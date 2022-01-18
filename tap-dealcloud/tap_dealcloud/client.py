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
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Charset': 'UTF-8',
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

    def get_rows(self):
        """Method for Data section Rows extraction"""

        prefix = 'data'
        url = "{base}/{version}/{prefix}/rows/view?api_key={key}".format(
            base=self.base_url, version=self.version, prefix=prefix, key=self.api_key)
        header = self.get_header()
        response = requests.get(url, headers=header, data=self.params)

        return response.json()['rows']

    def get_schema_data(self):
        """Method for schema data entries extraction"""

        prefix = 'schema'
        endpoints = ['users', 'currencies', 'allfields', 'fieldtypes', 'systemfieldtypes',
                     'systementrytypes', 'filteroperations', 'entrytypes', 'timezones']
        schemas = {}
        for endpoint in endpoints:
            try:
                url = "{base}/{version}/{prefix}/{endpoint}?api_key={key}".format(
                    base=self.base_url, version=self.version, prefix=prefix, endpoint=endpoint, key=self.api_key)
                header = self.get_header()
                response = requests.get(url, headers=header, data=self.params)
                schemas.update({endpoint: response.json()})
                #LOGGER.info("Fetching data for ", endpoint)
            except:
                LOGGER.info("Error in data extraction!")
                return
        # data = self.get_data()
        # schemas.update({"rows": data})

        return schemas
