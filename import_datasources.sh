#!/bin/bash

# Replace these variables with your actual values
token="eyJrIjoiZHFhODlGY2l6bGxVcGdyWmd4VmFqZVJnNndZeUplanAiLCJuIjoiYWRtaW4iLCJpZCI6MX0="
host="172.16.10.206:3000"


for FILE in *.json*; do
    echo -e ""
    echo -e "Importing Datasource:" $FILE
     cat $FILE | curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $token" "$host/api/datasources/" -d @- ;
done