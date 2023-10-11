#!/bin/bash

# Replace these variables with your actual values
token="eyJrIjoibU44TmVZNmJzbGdpVkRRclNPaEplRFhHeDFFWm1LVU0iLCJuIjoiYWRtaW4iLCJpZCI6MX0="
host="172.16.10.41:3000"


for FILE in *.json*; do
    echo -e ""
    echo -e "Importing Dashboard:" $FILE
    cat $FILE | jq '. * {overwrite: true, dashboard: {id: null}}' | curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $token" "$host/api/dashboards/db" -d @- ;
done