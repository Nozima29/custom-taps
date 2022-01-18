#!/usr/bin/env python3
import singer
from singer import utils

from tap_dealcloud.discover import discover
from tap_dealcloud.sync import sync

REQUIRED_CONFIG_KEYS = ["username", "password", "clientid", "api_key"]
LOGGER = singer.get_logger()


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
            catalog = discover(args.config)
        sync(args.config, args.state, catalog)


if __name__ == "__main__":
    main()
