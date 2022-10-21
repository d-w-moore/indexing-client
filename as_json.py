import sys,pprint,json
for x in sys.stdin:
    y = x.split(";;;")
    ID,MTIME,NAME,PARENT,SIZE = y[:5]
    SIZE=int(SIZE)
    data_size,is_file = max(SIZE,0),(SIZE >= 0)
    logical_path = "{PARENT}/{NAME}".format(**locals()) if is_file else NAME
    record = {"metadataEntries":list(
                  dict(zip(("attribute","value","unit"),y[4+j*3:7+j*3])) for j in
               range((len(y)-5)//3)
               )
             ,"dataSize": data_size
             ,"fileName": NAME
             ,"zoneName": logical_path.split("/",1)[0]
             ,"absolutePath": logical_path
             ,"lastModifiedDate": int(MTIME,10)
             ,"isFile":is_file
    }
    print(json.dumps(record,separators=(',',':')).rstrip("\n"))
