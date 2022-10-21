#!/bin/bash
Coll_Data_Size='-1'
if [[ $1 = [cC]* ]]; then
printf "collection's\n" >&2
QUERY="COLL_ID,COLL_MODIFY_TIME,COLL_NAME,COLL_PARENT_NAME where COLL_NAME like '$2/%' || = '$2'"
FMT="%s;;;%s;;;%s;;;%s;;;$Coll_Data_Size"
else
printf "data's\n" >&2
QUERY="DATA_ID,DATA_MODIFY_TIME,DATA_NAME,COLL_NAME,DATA_SIZE where COLL_NAME = '$2' || like '$2/%'"
FMT="%s;;;%s;;;%s;;;%s;;;%s"
fi
CMD="iquest --no-page '$FMT' \"select $QUERY\""
echo >&2 ---$'\n'"$CMD"$'\n---'
(eval "$CMD")
