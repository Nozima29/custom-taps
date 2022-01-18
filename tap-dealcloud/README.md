# tap-dealcloud

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from [FIXME](http://example.com)
- Extracts the following resources:
  - [FIXME](http://example.com)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

---

Copyright &copy; 2018 Stitch


schema endpoints: 
  1. users: "schema/users"
  2. currencies: "schema/currencies"
  3. allfields: "schema/allfields"
  4. fieldtypes: "schema/fieldtypes"
  5. systemfieldtypes: "schema/systemfieldtypes"
  6. systementrytypes: "schema/systementrytypes"
  7. filteroperations: "schema/filteroperations"
  8. entrytypes: "schema/entrytypes"
  9. timezones: "schema/timezones"

data endpoints:
  1. datarows: "data/rows/view"
  2. historyEntries: "data/entrydata/12/entries/history"