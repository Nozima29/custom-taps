from tap_movie import streams
import singer
from tap_movie.connect import MovieAPI

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
    api = MovieAPI(config["api_key"],
                   end_id=105)  # selecting only 5 (100-104) row data
    tap_data = api.fetch_data()
    for stream_name, endpoint_config in streams.STREAMS.items():
        LOGGER.info("Processing records for: {}".format(stream_name))
        write_schema(catalog, stream_name)
        singer.write_records(stream_name, tap_data)
        if endpoint_config.get("nested_entities"):
            for nested_entity in endpoint_config["nested_entities"].keys():
                for record in tap_data:
                    write_schema(catalog, nested_entity)
                    singer.write_records(nested_entity, record[nested_entity])

    return
