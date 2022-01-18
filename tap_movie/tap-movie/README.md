# tap-movie

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).


Running Tap:

    python3 -m venv ~/.virtualenvs/tap-movie
    source ~/.virtualenvs/tap-movie/bin/activate
    pip install tap-movie
    
    tap-movie -c config.json --catalog catalog.json --discover (for discover mode)

    or

    tap-movie -c config.json --catalog catalog.json
    (for sync mode)



