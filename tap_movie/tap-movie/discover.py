import os

from singer.catalog import Catalog, CatalogEntry
from singer.schema import Schema
from tap_movie.schema import get_schemas
from tap_movie.streams import STREAMS


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def discover(config):
    schemas, field_metadata = get_schemas(config, STREAMS)
    catalog = Catalog([])

    for stream_name, schema_dict in schemas.items():
        schema = Schema.from_dict(schema_dict)
        mdata = field_metadata[stream_name]["mdata"]
        catalog.streams.append(
            CatalogEntry(
                stream=stream_name,
                tap_stream_id=stream_name,
                key_properties=field_metadata[stream_name]["key_properties"],
                schema=schema,
                metadata=mdata,
            )
        )

    return catalog
