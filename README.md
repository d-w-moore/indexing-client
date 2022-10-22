# indexing-client

# 
```
ROOT_COLL="/tempZone/home/rods/v1"
{ bash get_objects.sh c "$ROOT_COLL"; bash get_objects.sh d "$ROOT_COLL" ; } |tee obj
python3 add_avus.py < obj |tee obj2
Then:
   * python3 as_json.py < obj2 > json.out
   or:
   * python
```
