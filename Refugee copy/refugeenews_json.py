#!/usr/bin/python3

import json, urllib.request, requests
from lxml import html

url = requests.get("https://api.reliefweb.int/v1/reports?appname=apidoc&query[value]=refugees&query[value]=women")

print(url.json())