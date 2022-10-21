#!/bin/bash
# This is very slow.  Use 'add_avus.py' instead.
DELIM=";;;"
while read LINE; do
    Y=($(sed "s/$DELIM/\n/g"<<<"$LINE"))
    if [ ${Y[4]} = "-1" ]; then
        t=COLL
    else
        t=DATA
    fi
    AVUs=$(iquest --no-page ';;;%s;;;%s;;;%s' "select order(META_${t}_ATTR_NAME), META_${t}_ATTR_VALUE, META_${t}_ATTR_UNITS where ${t}_ID = '${Y[0]}'")
    if [[ $AVUs =~ 'CAT_NO_ROWS' ]]; then AVUs="" 
    else
        AVUs=$(tr -d "\n" <<<"$AVUs")
    fi
    echo "$LINE$AVUs"
done
