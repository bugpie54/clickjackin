#!/bin/bash

#if [[$# -eq 0]]
#then
#echo "Usage: >./cjlist.sh <list.txt>"
#cho "Ex: ./cjlist.sh urls.txt"
#else

for url in $(cat $1)
do
	python3 cj.py $url
done
echo "[+] Test Complete!"
