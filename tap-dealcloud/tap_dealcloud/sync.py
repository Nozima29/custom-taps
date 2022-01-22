import singer
from datetime import datetime
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
    entries = client.get_entry_data()

    for stream_name, _ in streams.STREAMS.items():
        entry = entries[stream_name]
        if entry:
            LOGGER.info("Processing records for: {}".format(stream_name))
            write_schema(catalog, stream_name)
            singer.write_records(stream_name, entry)

    # state['last_sync_at'] = datetime.now()
    # singer.write_state(state)

    return
