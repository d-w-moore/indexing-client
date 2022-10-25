import base64
import json
import pprint
import sys
import getopt
from mime_table import get_mimetype

_DELIM = ';;;'

try:
    from shlex import quote
except ImportError:
    from pipes import quote

remove_cr = lambda List:List[:-1] + [elem.rstrip("\n") for elem in List[-1:]]

usage = False
try:
  opt,arg = getopt.getopt(sys.argv[1:],'f:H:N:P:',['help'])
except:
  usage = True

optD = dict(opt)

if usage or '--help' in optD: 
    print("usage:\t{sys.argv[0]} [[-H host] [-P port-number] [-N index-name]] | -f [format]".format(**locals()) +
          "\n\t""\t""example format: '{ID} {JSON}'.")
    exit()

PORT = int(optD.get('-P','9200'))
HOST = optD.get('-H','localhost')
NAME_OF_INDEX = optD.get('-N','metadata_index')

output_format = optD.get('-f')

if not output_format:
    output_format = '''curl -H "Content-Type: application/json" -X POST http://{HOST}:{PORT}/{NAME_OF_INDEX}/_doc/{ID} -d {SHELL_QUOTED_JSON}'''

for x in sys.stdin:
    y = x.split(_DELIM)
    ID,MTIME,NAME,PARENT,SIZE = y[:5]
    SIZE = int(SIZE)
    data_size,is_file = max(SIZE,0),(SIZE >= 0)
    logical_path = "{PARENT}/{NAME}".format(**locals()) if is_file else NAME
    record = {"metadataEntries":list(
                  dict(zip(("attribute","value","unit"),remove_cr(y[5+j*3:8+j*3]))) for j in
               range((len(y)-5)//3)
               )
             ,"dataSize": data_size
             ,"fileName": NAME
             ,"zoneName": logical_path.split("/",2)[1]
             ,"absolutePath": logical_path
             ,"lastModifiedDate": int(MTIME,10)
             ,"isFile":is_file
             ,"mimeType":get_mimetype(NAME)
             ,"url":"http:/"+logical_path
    }
    JSON = json.dumps(record,separators=(',',':')).rstrip("\n")
    SHELL_QUOTED_JSON = quote(JSON)
    print(output_format.format(**locals()))
