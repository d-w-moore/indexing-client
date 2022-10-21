import sys,pprint,json
remove_cr = lambda List:List[:-1] + [elem.rstrip("\n") for elem in List[-1:]]
for x in sys.stdin:
    y = x.split(";;;")
    ID,MTIME,NAME,PARENT,SIZE = y[:5]
    SIZE=int(SIZE)
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
    print(json.dumps(record,separators=(',',':')).rstrip("\n"))
