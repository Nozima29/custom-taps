from tap_dealcloud.discover import get_abs_path
from os import path
import requests
import base64
import json
import singer
import backoff

LOGGER = singer.get_logger()


class DealCloudError(Exception):
    def __init__(self, message=None, request=None):
        super().__init__(message)
        self.message = message
        self.request = request


class DealCloudAuthError(DealCloudError):
    pass


ERROR_CODE_EXCEPTION_MAPPING = {
    401: {
        "raise_exception": DealCloudAuthError,
        "message": "Invalid auth credentials."
    }
}


class DealCloudClient:
    def __init__(self, config, state=None):
        self.clientid = config["clientid"]
        self.api_key = config["api_key"]
        self.account = config["account"]
        self.base_url = f"https://{self.account}.dealcloud.com/api/rest"
        self.token_url = self.base_url+"/v1/oauth/token"
        self.state = state

    @property
    def basic_token(self):
        base_token = f"{self.clientid}:{self.api_key}"
        base_token = base_token.encode('ascii')
        base_token = base64.b64encode(base_token)
        base_token = base_token.decode('ascii')
        return base_token

    @backoff.on_exception(
        backoff.expo,
        (requests.exceptions.RequestException,
         DealCloudAuthError),
        max_tries=5,
        factor=2)
    def get_oauth_token(self):
        payload = 'Scope=data&grant_type=client_credentials'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Basic {}'.format(self.basic_token)
        }
        response = requests.request(
            "POST", self.token_url, headers=headers, data=payload)
        res_dict = json.loads(response.text)
        token = res_dict["access_token"]
        return token

    def get_header(self):
        token = self.get_oauth_token()
        header = {'Authorization': 'Bearer ' + token}
        return header

    @backoff.on_exception(
        backoff.expo,
        (requests.exceptions.RequestException,
         DealCloudAuthError),
        max_tries=5,
        factor=2)
    def make_request(self, url):
        header = self.get_header()
        response = requests.get(url, headers=header)
        return response

    def write_entrytypes(self, f_name, data):
        """
        Method for writing/saving all existing entrytypes (tables) with IDs in order to avoid 
        multiple access in each api call
        format:
            {
                "table_name": "table_id"
            }
        """
        json_data = dict()
        with open(f_name, 'w') as wf:
            for entry in data:
                json_data.update({entry["apiName"]: entry["id"]})
            json_object = json.dumps(json_data, indent=3)
            wf.write(json_object)

    def get_entrytype(self, stream_name):
        """
        Method for getting and saving all registered table names with corresponding ID
        return: ID of a single table (entrytype)
        """

        entry_data = None
        prefix = 'schema'
        endpoint = 'entrytypes'
        assets = get_abs_path('assets.json')
        if path.exists(assets):
            with open(assets, 'r') as rf:
                json_data = rf.read()
                json_data = json.loads(json_data)
                entry_data = json_data[stream_name]
        else:
            try:
                url = "{base}/v4/{prefix}/{endpoint}?api_key={key}".format(
                    base=self.base_url, prefix=prefix, endpoint=endpoint, key=self.api_key)
                response = self.make_request(url)
            except DealCloudAuthError as err:
                raise err
            entries = response.json()
            self.write_entrytypes(assets, entries)

            for entry in entries:
                if entry["apiName"] == stream_name:
                    entry_data = entry["id"]

        return entry_data

    def get_updates(self, entrytype, stream_name):
        """Method for returning updated/deleted/inserted records"""

        updates = None
        url = "{base}/v4/data/entrydata/{entryTypeId}/entries/history?modifiedSince={state}&api_key={key}".format(
            base=self.base_url, state=self.state["last_sync_at"],
            entryTypeId=entrytype, key=self.api_key)
        response = self.make_request(url)
        entry = response.json()
        if entry:
            updates, del_rec, updated_rec, new_rec = self.find_updated_row(
                entry)
            LOGGER.info(
                f"Found {del_rec} deletion(s), {updated_rec} update(s), {new_rec} insertion(s) for {stream_name}")
        if updates:
            return updates

    def find_updated_row(self, entry):
        """
        Helper function for get_updates() method
        Fetches corresponding updated data
        """
        data = list()
        deleted_records_count = 0
        updated_records_count = 0
        inserted_records_count = 0

        for e in entry:
            if e["isDeleted"] == True:
                deleted_records_count += 1
                data.append({
                    "EntryId": e["id"],
                    "_sdc_deleted_at": True
                })
            else:
                ent = self.get_rows(e["entryListId"], e["id"])
                if ent["CreatedDate"] == ent["ModifiedDate"]:
                    inserted_records_count += 1
                else:
                    updated_records_count += 1

                if isinstance(ent, dict):
                    data.append(ent)
        return data, deleted_records_count, updated_records_count, inserted_records_count

    def get_rows(self, entrytype, entryId=None):
        """Method for getting all data rows (entries)"""

        entries = None
        prefix = 'data/entrydata/rows'
        try:
            url = "{base}/v4/{prefix}/{entryTypeId}?api_key={key}".format(
                base=self.base_url, prefix=prefix, entryTypeId=entrytype, key=self.api_key)
            response = self.make_request(url)
            entry = response.json()

        except DealCloudAuthError as err:
            raise err
        if "rows" in entry.keys():
            entries = entry.get("rows")
            if entryId:
                for entry in entries:
                    if entry["EntryId"] == entryId:
                        return entry

        else:
            entries = entry

        return entries

    def get_data(self, stream_name):
        entrytype = self.get_entrytype(stream_name)

        if self.state:
            data = self.get_updates(entrytype, stream_name)

        else:
            data = self.get_rows(entrytype)
            LOGGER.info("{} records to be migrated to {}".format(
                len(data), stream_name))

        return data
