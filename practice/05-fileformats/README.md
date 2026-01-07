# Working with file formats and cleaning data

## Convert Delimiters

To convert TSV to CSV, or vice versa, use a text search+replace function such as `awk`, `tr`, or a good IDE/text editor:

### tr
```
tr '\t' ',' < file.tsv > file.csv
```

### sed
```
sed 's/'$'\t''/,/g' file.tsv > file.csv
```

### awk
```
awk 'BEGIN { FS="\t"; OFS="," } {$1=$1; print}' file.tsv > file.csv
```

This folder contains a CSV and TSV file. Try converting the format of one to another.

## Consuming Logs

[Parse/Filter Logs using Python](https://www.kaggle.com/nealmagee/parse-logs)

## Data Cleaning Exercises

Kaggle offers some data cleaning tutorials and exercises:

1. [Handling Missing Values](https://www.kaggle.com/alexisbcook/handling-missing-values)
2. [Scaling and Normalization](https://www.kaggle.com/alexisbcook/scaling-and-normalization)
3. [Parsing Dates](https://www.kaggle.com/alexisbcook/parsing-dates)
4. [Character Encoding](https://www.kaggle.com/alexisbcook/character-encodings)
5. [Inconsistent Data](https://www.kaggle.com/alexisbcook/inconsistent-data-entry)


## json

Some iterations to try using the `jq` tool in the command-line:

Filter the `mock_data.json` file containing "flat", non-nested data.
```
cd /root/course/01-data/
cat mock_data.json
cat mock_data.json | jq -r .[]
cat mock_data.json | jq -r .[] | jq ."dob"
cat mock_data.json | jq -r .[] | jq ."dob" | grep "1998"
cat mock_data.json | jq -r .[] | jq ."dob" | grep "1998" | wc -l
```

Filter the `mock_data_nested.json` file containing nested data.
```
cd /root/course/01-data/
cat mock_data_nested.json
cat mock_data_nested.json | jq ."healthChecks"
cat mock_data_nested.json | jq ."healthChecks" | jq .[]."delaySeconds"
cat mock_data_nested.json | jq ."healthChecks" | jq -r .[]."delaySeconds"
```

```
cd /root/course/01-data/
cat mock_data_nested.json | jq ."container"
cat mock_data_nested.json | jq ."container" | jq ."volumes"
cat mock_data_nested.json | jq ."container" | jq ."volumes" | jq -r .[]."hostPath"
```

Notice the `-r` flag to toggle "raw" output versus quote-wrapped output.

Explore [jq play](https://jqplay.org) for more lessons, inputs, filters, etc.

## Using Python to Parse JSON

Try the notebook based [Kaggle Lab](https://www.kaggle.com/nealmagee/parsing-json).

## csv

```
cat mock_data.csv
```

Note that the 6 columns are separated by 5 commas. Fields that must contain a comma should be quote-enclosed.

## tsv

Like CSV files separated by commas, tab-separated files are delimited by tabs. This can fool the naked eye, and throw off import
processes when stray tabs are inserted into the data fields.

To convert TSV to CSV, or vice versa, use a text search+replace function such as `awk`, `tr`, or a good IDE/text editor:

### tr
```
tr '\t' ',' < file.tsv > file.csv
```

### sed
```
sed 's/'$'\t''/,/g' file.tsv > file.csv
```

### awk
```
awk 'BEGIN { FS="\t"; OFS="," } {$1=$1; print}' file.tsv > file.csv
```

## xml

Structured data. Note that every record, and every data field within each record, is fully wrapped in markup that is opened and closed:

```xml
<dataset>
  . . .
  <record>
    <id>97</id>
    <first_name>Tamarra</first_name>
    <last_name>Jeannaud</last_name>
    <email>tjeannaud2o@fema.gov</email>
    <ip_address>26.106.176.174</ip_address>
    <dob>11/19/1981</dob>
  </record>
  <record>
    <id>98</id>
    <first_name>Korney</first_name>
    <last_name>Hazlegrove</last_name>
    <email>khazlegrove2p@wsj.com</email>
    <ip_address>218.117.101.96</ip_address>
    <dob>01/06/1981</dob>
  </record>
  . . .
</dataset>
```

## sql

`cat` and `head` and `tail` the SQL snippet. Notice that each line consists of an isolated query.
The SQL file is therefore not a bulk insert statement (not properly) but a concatenated series of independent
SQL statements. This is a best practice so that any single line that triggers a failure can be more
easily identified and the previous inserts will have succeeded.

```
INSERT INTO mock_data_tbl (id, first_name, last_name, email, ip_address, dob) VALUES (1, 'Berkley', 'Annon', 'bannon0@accuweather.com', '193.95.255.138', '10/20/1991');
INSERT INTO mock_data_tbl (id, first_name, last_name, email, ip_address, dob) VALUES (2, 'Doro', 'Morse', 'dmorse1@moonfruit.com', '170.67.183.172', '12/01/1995');
INSERT INTO mock_data_tbl (id, first_name, last_name, email, ip_address, dob) VALUES (3, 'Charmain', 'Halden', 'chalden2@europa.eu', '170.112.37.136', '03/03/1982');
INSERT INTO mock_data_tbl (id, first_name, last_name, email, ip_address, dob) VALUES (4, 'Allissa', 'Wakefield', 'awakefield3@usgs.gov', '23.46.25.161', '10/05/1988');
```

# Working with remote data

## Fetch Remote Data using `curl` and `jq`

### Replace USER with your GitHub username
```
curl https://api.github.com/users/USER/events
```

### Scroll through events
```
curl https://api.github.com/users/nmagee/events | jq .[] | less
```

### Filter out values:
```
curl https://api.github.com/users/nmagee/events | jq .[].id
curl https://api.github.com/users/nmagee/events | jq .[].payload.commits
curl https://api.github.com/users/nmagee/events | jq .[].payload.commits | jq .[].message
```

### Format output:
```
curl 'https://api.github.com/repos/stedolan/jq/commits'
curl 'https://api.github.com/repos/stedolan/jq/commits' \
   | jq '.[] | {message: .commit.message, name: .commit.committer.name}'
```

There are plenty of other examples in the tutorial at https://stedolan.github.io/jq/tutorial/

## Tools for Retrieving Data

`curl` - is a common Linux-based tool to fetch raw files. You've been using it in the exercises above.
```
curl https://www.virginia.edu/ > index.html
```

`wget` - another common Linux-based tool, similar to `curl`.
```
wget https://www.virginia.edu/
```

`http` - runs the HTTPie tool to fetch web resources:
```
http --head https://www.virginia.edu/
http --body https://www.virginia.edu/
```

Windows 10 and above come with `curl.exe` installed:
```
# example 1
curl.exe --output index.html --url https://superuser.com
# example 2
curl.exe -o index.html https://superuser.com
```

## Advanced Concepts

### Streaming Large Files

When working with very large files that don't fit in memory, you need to process them in chunks rather than loading everything at once. Python's `pandas` library supports chunking:

```python
import pandas as pd

# Process CSV in chunks
chunk_size = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # Process each chunk
    process(chunk)
```

For JSON files, use streaming parsers like `ijson`:

```python
import ijson

# Stream parse large JSON files
with open('large_file.json', 'rb') as f:
    parser = ijson.items(f, 'item')
    for item in parser:
        process(item)
```

### Schema Validation

Validating data against a schema ensures data quality and catches errors early. For JSON, use JSON Schema:

```python
import jsonschema

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name", "age"]
}

jsonschema.validate(instance=data, schema=schema)
```

For CSV files, consider using libraries like `pandera` or `great-expectations` for data validation.

### Binary and Columnar Formats

For better performance with large datasets, consider binary formats:

- **Parquet**: Columnar storage format, excellent for analytics workloads. Supports compression and schema evolution.
- **Avro**: Row-based binary format with schema evolution support.
- **Protocol Buffers**: Google's language-neutral, platform-neutral serialization format.

These formats offer:
- Better compression ratios
- Faster read/write performance
- Schema evolution support
- Type safety

Example with Parquet:
```python
import pandas as pd

# Write to Parquet
df.to_parquet('data.parquet', compression='snappy')

# Read from Parquet
df = pd.read_parquet('data.parquet')
```

## Resources

### File Format Documentation

* [JSON Specification](https://www.json.org/json-en.html) - Official JSON format specification
* [CSV RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180) - CSV format standard
* [XML Specification](https://www.w3.org/XML/) - W3C XML documentation

### Tools and Libraries

* [jq Manual](https://stedolan.github.io/jq/manual/) - Complete jq documentation and tutorial
* [jq Play](https://jqplay.org/) - Interactive jq playground
* [Pandas Documentation](https://pandas.pydata.org/docs/) - Python data manipulation library
* [Apache Parquet](https://parquet.apache.org/) - Columnar storage format documentation

### Data Cleaning and Validation

* [Great Expectations](https://greatexpectations.io/) - Data validation framework
* [Pandera](https://pandera.readthedocs.io/) - Statistical data validation for pandas
* [JSON Schema](https://json-schema.org/) - Schema validation for JSON

### API and Web Data

* [HTTPie Documentation](https://httpie.io/docs) - Command-line HTTP client
* [curl Manual](https://curl.se/docs/manual.html) - Complete curl documentation
* [GitHub API Documentation](https://docs.github.com/en/rest) - Working with GitHub's REST API
