import singer
from datetime import datetime
from tap_dealcloud.client import DealCloudClient
from tap_dealcloud import streams

LOGGER = singer.get_logger()


def write_state(state, last_sync_at):
    state['last_sync_at'] = last_sync_at.strftime('%Y-%m-%dT%H:%M:%S')
    try:
        singer.write_state(state)
    except OSError as err:
        LOGGER.info('Error in writing state')
        raise err


def sync(config, state, catalog):
    client = DealCloudClient(config)
    entries = client.get_entry_data()
    last_sync_at = datetime.now()
    for stream_name, _ in streams.STREAMS.items():
        entry = entries[stream_name]
        LOGGER.info("Processing records for: {}".format(stream_name))
        stream = catalog.get_stream(stream_name)
        schema = stream.schema.to_dict()
        singer.write_schema(stream_name, schema, stream.key_properties)
        singer.write_records(stream_name, entry)

    write_state(state, last_sync_at)

    return
