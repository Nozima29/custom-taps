#!/usr/bin/env python3
import singer
from singer import utils

from tap_movie.discover import discover
from tap_movie.sync import sync

LOGGER = singer.get_logger()
REQUIRED_CONFIG_KEYS = ["api_key"]


@utils.handle_top_exception(LOGGER)
def main():
    args = utils.parse_args(REQUIRED_CONFIG_KEYS)

    if args.discover:
        catalog = discover(args.config)
        catalog.dump()
    else:
        if args.catalog:
            catalog = args.catalog
        else:
            catalog = discover()
        sync(args.config, args.state, catalog)


if __name__ == "__main__":
    main()
