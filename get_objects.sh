#!/bin/bash
DELIM=';;;'
Coll_Data_Size='-1'
if [[ $1 = [cC]* ]]; then
    #printf "collections\n" >&2
    QUERY="COLL_ID,COLL_MODIFY_TIME,COLL_NAME,COLL_PARENT_NAME where COLL_NAME like '$2/%' || = '$2'"
    FMT="%s${DELIM}%s${DELIM}%s${DELIM}%s${DELIM}$Coll_Data_Size"
else
    #printf "datas\n" >&2
    QUERY="DATA_ID,DATA_MODIFY_TIME,DATA_NAME,COLL_NAME,DATA_SIZE where COLL_NAME = '$2' || like '$2/%'"
    FMT="%s${DELIM}%s${DELIM}%s${DELIM}%s${DELIM}%s"
fi
CMD="iquest --no-page '$FMT' \"select $QUERY\""
#echo >&2 ---$'\n'"$CMD"$'\n---'
eval "$CMD"
