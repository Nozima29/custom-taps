from tap_dealcloud.discover import get_abs_path
from os import path
import requests
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
        self.username = config['username']
        self.password = config['password']
        self.clientid = config['clientid']
        self.api_key = config['api_key']
        self.base_url = config['base_url']
        self.token_url = config['token_url']
        self.header_basic = config['header_basic']
        self.version = config['version']
        self.state = state

    @property
    def params(self):
        return {
            "username": self.username,
            "password": self.password,
            "clientid": self.clientid
        }

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
            'Authorization': 'Basic {}'.format(self.header_basic)
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
        response = requests.get(url, headers=header, data=self.params)
        return response

    def write_entrytypes(self, f_name, data):
        json_data = dict()
        with open(f_name, 'w') as wf:
            for entry in data:
                json_data.update({entry["apiName"]: entry["id"]})
            json_object = json.dumps(json_data, indent=3)
            wf.write(json_object)

    def get_entrytype(self, stream_name):
        """
        Methods for getting and saving all registered table names with corresponding ID
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
                url = "{base}/{version}/{prefix}/{endpoint}?api_key={key}".format(
                    base=self.base_url, version=self.version, prefix=prefix, endpoint=endpoint, key=self.api_key)
                response = self.make_request(url)
            except DealCloudAuthError as err:
                raise err
            entries = response.json()
            self.write_entrytypes(assets, entries)

            for entry in entries:
                if entry["apiName"] == stream_name:
                    entry_data = entry["id"]

        return entry_data

    def get_updates(self, entrytype):
        data = []
        url = "{base}/{version}/data/entrydata/{entryTypeId}/entries/history?modifiedSince={state}&api_key={key}".format(
            base=self.base_url, version=self.version, state=self.state["last_sync_at"],
            entryTypeId=entrytype, key=self.api_key)
        response = self.make_request(url)
        entry = response.json()
        if entry:
            data = self.find_updated_row(entry, data)
        if data:
            return data

    def find_updated_row(self, entry, data):
        for e in entry:
            if e["isDeleted"] == True:
                data.append(
                    {"EntryId": e["id"], "_sdc_deleted_at": True})
            else:
                ent = self.get_rows(e["entryListId"], e["id"])
                if isinstance(ent, dict):
                    data.append(ent)
        return data

    def get_rows(self, entrytype, entryId=None):
        entries = None
        prefix = 'data/entrydata/rows'
        try:
            url = "{base}/{version}/{prefix}/{entryTypeId}?api_key={key}".format(
                base=self.base_url, version=self.version, prefix=prefix,
                entryTypeId=entrytype, key=self.api_key)

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
            data = self.get_updates(entrytype)

        else:
            data = self.get_rows(entrytype)

        return data
