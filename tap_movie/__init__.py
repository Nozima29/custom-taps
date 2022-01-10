#!/usr/bin/env python3
import os
import json
import singer
from singer import utils
from singer.catalog import Catalog, CatalogEntry
from singer.schema import Schema

from tap_movie.connect import MovieConnect


REQUIRED_CONFIG_KEYS = ["start_date", "api_key"]
LOGGER = singer.get_logger()
API_KEY = "a463e23f4a85ede8714949bc767318b5"


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def load_schemas():
    """Load schemas from schemas folder"""
    schemas = {}
    # for filename in os.listdir(get_abs_path("schemas")):
    path = get_abs_path("schemas") + "/movie.json"  # + filename
    # file_raw = filename.replace(".json", "")
    with open(path) as file:
        schemas[path] = Schema.from_dict(json.load(file))
    return schemas


def discover():
    raw_schemas = load_schemas()
    streams = []
    for stream_id, schema in raw_schemas.items():
        stream_metadata = []
        key_properties = []
        streams.append(
            CatalogEntry(
                tap_stream_id=stream_id,
                stream=stream_id,
                schema=schema,
                key_properties=key_properties,
                metadata=stream_metadata,
                replication_key=None,
                is_view=None,
                database=None,
                table=None,
                row_count=None,
                stream_alias=None,
                replication_method=None,
            )
        )
    return Catalog(streams)


def sync(config, state, catalog):
    """Sync data from tap source"""
    # Loop over selected streams in catalog

    for stream in catalog.get_selected_streams(state):

        LOGGER.info("Syncing stream:" + stream.tap_stream_id)

        bookmark_column = stream.replication_key
        is_sorted = True

        singer.write_schema(
            stream_name=stream.tap_stream_id,
            schema=stream.schema.to_dict(),
            key_properties=stream.key_properties,
        )

        client = MovieConnect(API_KEY, end_id=120)
        tap_data = client.fetch_data()
        max_bookmark = None
        for row in tap_data:
            singer.write_records(stream.tap_stream_id, [row])
            if bookmark_column:
                if is_sorted:
                    singer.write_state({stream.tap_stream_id: row[bookmark_column]})
                else:
                    max_bookmark = max(max_bookmark, row[bookmark_column])
        if bookmark_column and not is_sorted:
            singer.write_state({stream.tap_stream_id: max_bookmark})
    return


@utils.handle_top_exception(LOGGER)
def main():
    args = utils.parse_args(REQUIRED_CONFIG_KEYS)

    if args.discover:
        catalog = discover()
        catalog.dump()
    else:
        if args.catalog:
            catalog = args.catalog
        else:
            catalog = discover()
        sync(args.config, args.state, catalog)


if __name__ == "__main__":
    main()
