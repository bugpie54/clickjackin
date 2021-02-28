#!/bin/bash

if [[ -z "$1" ]]
then
echo "Usage:> ./cjlist.sh <list.txt>"
echo "Ex: ./cjlist.sh urls.txt"
else
for url in $(cat $1)
do
python3 cj.py "$url"
done
echo "[+] Test Complete!"
fi
