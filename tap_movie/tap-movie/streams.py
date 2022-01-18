STREAMS = {
    "movie": {
        "key_properties": [
            "id"
        ],
        "replication_method": "FULL_TABLE",
        "nested_entities": {
            "genres": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "production_companies": {
                "key_properties": [
                    "id"
                ],
                "replication_method": "FULL_TABLE"
            },
            "production_countries": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            },
            "spoken_languages": {
                "key_properties": [
                    "name"
                ],
                "replication_method": "FULL_TABLE"
            }
        }
    }
}
