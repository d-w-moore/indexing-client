# indexing-client

# Index iRODS system metadata and AVUS under a $ROOT_COLLECTION
# Commands 
```
ROOT_COLL="/tempZone/home/rods/v1"

{ bash get_objects.sh c "$ROOT_COLLECTION"; bash get_objects.sh d "$ROOT_COLLECTION" ; } | tee objs

python3 add_avus.py < objs | tee objs_with_avus

Then:

   * python3 as_json.py -f '{ID} {JSON}' < objs_with_avus | while read id json; do [...] ; done

   or:

   * python3 as_json -H host -P port -N index-name < objs_with_avus
```
