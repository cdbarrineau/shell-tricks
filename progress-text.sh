#!/bin/bash

for i in 1 2 3 4 5
do 
  echo -ne "\r$(tput el)Your new text: $i"
  sleep 1
done
