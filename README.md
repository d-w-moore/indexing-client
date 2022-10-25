# indexing-client

Index iRODS system metadata and AVUS under a $ROOT_COLLECTION

## Purpose

To generate the JSON content, or Bash commands, necessary to index all objects under a root collection.

This is accomplished using iRODS clients instead of through the normal policy mechanisms of the iRODS Indexing Plugin.

The python-irodsclient is required for best results. v1.1.5 was used during test, although pre-v1.0 versions should
work as well.

## Commands 

Do the following to generate records of catalog objects complete with system metadata and AVU's:
```
ROOT_COLLECTION="/tempZone/home/rods/v1"
{ bash get_objects.sh c "$ROOT_COLLECTION"; bash get_objects.sh d "$ROOT_COLLECTION" ; } | tee objs
python3 add_avus.py < objs | tee objs_with_avus
```

Then, either:
```
python3 metadata_as_json.py -f '{ID} {JSON}' < objs_with_avus | while read id json; do [...] ; done
```
which would generate custom-formatted records with the object ID in the ICAT db, followed by the literal JSON for the index request, 
and pipe that through custom processing via the variables $id and $json in a Bash loop.

Or (even better) to output as a batch file of curl commands compatible with sh/Bash and gnu Parallel.
```
   * python3 metadata_as_json.py -H [host] -P [port] -N [index-name] < objs_with_avus > curl_commands
```
