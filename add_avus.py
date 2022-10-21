#!/usr/bin/env python3
from irods.test.helpers import make_session
from irods.models import Collection,DataObject
from irods.models import CollectionMeta,DataObjectMeta
import sys

DELIM=';;;'

def str_from_all_avus(iter_, delim = DELIM):
  return ''.join( (delim + elem) for i in iter_ for elem in i )

s = make_session( )

meta_cols = { m:(m.name,m.value,m.units) for m in (DataObjectMeta,CollectionMeta) }

for line in sys.stdin:
    Y=line.split(DELIM)
    flag_or_size = int(Y[4])
    is_file = (flag_or_size >= 0)
    obj_model,meta_model = (DataObject,DataObjectMeta) if is_file else (Collection,CollectionMeta)
    cols = meta_cols[meta_model] + (obj_model.id,)
    q = s.query(*cols).filter(obj_model.id == Y[0])
    avus=(tuple(row[i] for i in cols[:3]) for row in q)
    sys.stdout.write(line.rstrip('\n') + str_from_all_avus(avus) + "\n")#; sys.stdout.flush()
