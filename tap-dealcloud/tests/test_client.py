from tap_dealcloud.client import DealCloudClient
import unittest
import json


class TestDealcloudClient(unittest.TestCase):
    def setUp(self):
        config_file = "client_config.json"
        with open(config_file, "r") as rf:
            config = json.loads(rf.read())
        self.instance = DealCloudClient(config)

    def test_entrytype_id(self):
        stream_name = "Deal"
        with open("tap_dealcloud/assets.json", "r") as rf:
            data = rf.read()
            data = json.loads(data)
            id = data[stream_name]
        stream_id = self.instance.get_entrytype(stream_name)
        print("nozzzzzz")
        self.assertEqual(stream_id, id)

    def test_entry_document(self):
        stream_name = "Document"
        data = self.instance.get_data(stream_name)
        self.assertTrue(len(data) > 0)

    def test_entry_users(self):
        stream_name = "User"
        data = self.instance.get_data(stream_name)
        self.assertTrue(len(data) > 0)


if __name__ == '__main__':
    unittest.main()
