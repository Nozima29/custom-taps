import json
import singer

from tap_dealcloud.client import DealCloudClient
from tap_dealcloud import streams

LOGGER = singer.get_logger()


def write_schema(catalog, stream_name):
    stream = catalog.get_stream(stream_name)
    schema = stream.schema.to_dict()
    try:
        singer.write_schema(stream_name, schema, stream.key_properties)
    except OSError as err:
        LOGGER.info("OS Error writing schemas for: {}".format(stream_name))
        raise err


def sync(config, state, catalog):
    client = DealCloudClient(config)
    data = client.get_schema_data()

    for stream_name, endpoint_config in streams.STREAMS.items():
        # print(stream_name)
        # data = data[stream_name.lower()]
        # print(data[stream_name.lower()])
        LOGGER.info("Processing records for: {}".format(stream_name))
        write_schema(catalog, stream_name)
        singer.write_records(stream_name, data[stream_name.lower()])
        if endpoint_config.get("nested_entities"):
            for nested_entity in endpoint_config["nested_entities"].keys():
                for rec in data[stream_name.lower()]:
                    if nested_entity in rec.keys():
                        if rec[nested_entity]:
                            # print(rec[nested_entity])
                            write_schema(catalog, nested_entity)
                            singer.write_records(
                                nested_entity, rec[nested_entity])

    return
