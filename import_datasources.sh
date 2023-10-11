#!/bin/bash

# Replace these variables with your actual values

token = "<your-grafana-token>"
host = "<ip-address>:<port>"


for FILE in *.json*; do
    echo -e ""
    echo -e "Importing Datasource:" $FILE
     cat $FILE | curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $token" "$host/api/datasources/" -d @- ;
done
