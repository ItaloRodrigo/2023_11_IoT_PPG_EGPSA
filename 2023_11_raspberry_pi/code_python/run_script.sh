#!/bin/bash

python_status=$?

current_date=`date "+%D %T"`

msg="Informações:  

Server: $HOSTNAME

Script Name: $1 

Time: $current_date"

echo "$python_status"
echo "$msg"

source "/home/italo/Desktop"

simulador_dispositivo_iot.py