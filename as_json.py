import base64
import json
import pprint
import sys
import getopt

try:
    from shlex import quote
except ImportError:
    from pipes import quote

remove_cr = lambda List:List[:-1] + [elem.rstrip("\n") for elem in List[-1:]]

opt,arg = getopt.getopt(sys.argv[1:],'qvf:')
optD = dict(opt)

output_format = optD.get('-f')

if not output_format:
    output_format = '''curl -H "Content-Type: application/json" -X POST http://localhost:9200/metadata_idx/_doc/{ID} -d {SHELL_QUOTED_JSON}'''

if '-v' in optD:
    print ('output_format =',output_format, file = sys.stderr)

if '-q' in optD:
    exit()

for x in sys.stdin:
    y = x.split(";;;")
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
    }
    JSON = json.dumps(record,separators=(',',':')).rstrip("\n")
    SHELL_QUOTED_JSON = quote(JSON)
    print(output_format.format(**locals()))
