# redate.py

Set the correct date on google photos dumps from google takeout.

Dumps from Google Takeout do not include time metadata. However, for Google Photos at least, they use the file's UTC timestamp in the files name.

This command line program recursively walks the provided path, changing each file's created and accessed time to match the datetime, if one is specified in the file
name e.g... IMG_20190527_152734857.jpg

## Usage...

```bash
	python3 redate.py <optional path to a folder>
```

The current working directory is used as the start point if a source path is not provided.