import requests
import singer

LOGGER = singer.get_logger()


class MovieAPI:
    def __init__(self, key, end_id, start_id=100):
        self.start_id = start_id
        self.end_id = end_id
        self.key = key
        self.url = "https://api.themoviedb.org/3/movie/"

    def fetch_data(self):
        data = []
        id = self.start_id
        while id < self.end_id:
            url = self.url + "{}?api_key={}".format(id, self.key)
            try:
                client = requests.get(url)
                LOGGER.info("Fetching data from {}".format(url))
                # json_object = json.dumps(client.json(), indent=4)
                data.append(client.json())
                id += 1
            except:
                LOGGER.info("Error in connecting to {}".format(url))

        return data
