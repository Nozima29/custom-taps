import os
import json
from singer import metadata


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def get_schemas(config, streams):
    schemas = {}
    field_metadata = {}
    selected_all = config.get("selected_all", False)

    for stream_name, stream_metadata in streams.items():
        schema_path = get_abs_path("schemas/{}.json".format(stream_name))
        with open(schema_path, encoding="utf8") as file:
            schema = json.load(file)
        schemas[stream_name] = schema
        mdata = metadata.new()
        mdata = metadata.get_standard_metadata(
            schema=schema,
            key_properties=stream_metadata.get("key_properties", None),
            valid_replication_keys=stream_metadata.get(
                "replication_keys", None),
            replication_method=stream_metadata.get("replication_method", None),
        )
        if selected_all:
            for m in mdata:
                m["metadata"]["selected"] = True
        field_metadata[stream_name] = {}
        field_metadata[stream_name]["mdata"] = mdata
        field_metadata[stream_name]["key_properties"] = stream_metadata.get(
            "key_properties", None
        )

        if (
            "nested_entities" in stream_metadata.keys()
            and stream_metadata["nested_entities"]
        ):
            nested_schemas, nested_field_metadata = get_schemas(
                config, stream_metadata["nested_entities"]
            )
            schemas.update(nested_schemas)
            field_metadata.update(nested_field_metadata)

    return schemas, field_metadata
