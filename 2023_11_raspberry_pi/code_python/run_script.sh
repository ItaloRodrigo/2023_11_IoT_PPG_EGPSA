#!/bin/bash
source "/home/italo/Desktop"

python3 $1

python_status=$?

current_date=`date "+%D %T"`

msg="Informações:  

Server: $HOSTNAME

Script Name: $1 

Time: $current_date"

echo "$python_status"
echo "$msg"

