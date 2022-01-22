import requests
import json
import singer

LOGGER = singer.get_logger()


class DealCloudClient:
    def __init__(self, config):
        self.username = config['username']
        self.password = config['password']
        self.clientid = config['clientid']
        self.api_key = config['api_key']
        self.base_url = config['base_url']
        self.token_url = config['token_url']
        self.header_basic = config['header_basic']
        self.version = config['version']

    @property
    def params(self):
        return {
            "username": self.username,
            "password": self.password,
            "clientid": self.clientid
        }

    def get_oauth_token(self):
        payload = 'Scope=data&grant_type=client_credentials'
        headers = {
            'Content-Type': 'application/json',
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

    def make_request(self, url):
        header = self.get_header()
        response = requests.get(url, headers=header, data=self.params)
        return response

    def get_entrytypes(self):
        prefix = 'schema'
        endpoint = 'entrytypes'
        try:
            url = "{base}/{version}/{prefix}/{endpoint}?api_key={key}".format(
                base=self.base_url, version=self.version, prefix=prefix, endpoint=endpoint, key=self.api_key)
            response = self.make_request(url)
        except:
            LOGGER.info(f"Error in {endpoint} extraction!")
            return

        return response.json()

    def get_entry_data(self):
        prefix = 'data/entrydata/rows'
        data = dict()
        entrytypes = self.get_entrytypes()
        for entrytype in entrytypes:
            try:
                url = "{base}/{version}/{prefix}/{entryTypeId}?api_key={key}".format(
                    base=self.base_url, version=self.version, prefix=prefix,
                    entryTypeId=entrytype['id'], key=self.api_key)

                response = self.make_request(url)
                entry = response.json()

                LOGGER.info(f"Fetched data for {entrytype['apiName']}")

            except:
                LOGGER.info("Error in entrydata extraction!")
                return

            if entry["rows"] and isinstance(entry["rows"], list):
                data[entrytype["apiName"]] = entry.get("rows")
                # print(data)

        return data
