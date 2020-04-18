#!/usr/bin/env python3

import argparse
import urllib.parse
import webbrowser

sArgParser=argparse.ArgumentParser(description='Search Google for a search term with different websites. Use escaped quotes when necessary: \\\"')
sArgParser.add_argument('-c', metavar="<count>", help='How many websites checked per query. Google has a maximum length for queries.')
#sArgParser.add_argument('-e', metavar="<engine>", help='Search with \'google\' or \'bing\', defaults to \'google\'.', choices=['bing', 'google', 'yahoo'], default="google")
sArgParser.add_argument('-f', metavar="<file>", help='Enter a custom website list.')
sArgParser.add_argument('-s', metavar="<status>",help='Enable or disable the \'site:\' operator, defaults to \'enable\'.',default='enable', choices=['enable', 'disable'])
sArgParser.add_argument('-q', metavar="<query>",  help='Enter a search term.')
aArguments=sArgParser.parse_args()

if not aArguments.q:
    sQuery = ""
else:
    sQuery = urllib.parse.quote(aArguments.q)


if aArguments.c:
    iNewUrlAfter = int(aArguments.c)
else:
    iNewUrlAfter = 30

if aArguments.f:
    sInputFile = aArguments.f
else:
    sInputFile = "dorkdomains.txt"

if aArguments.s == "enable":
    sSite = "site:"
else:
    sSite = ""

sQuery = "https://www.google.com/search?num=100&filter=0&q=" + sQuery

'''
if aArguments.e == "google":
    sQuery = "https://www.google.com/search?num=100&filter=0&q=" + urllib.parse.quote(aArguments.q)
elif aArguments.e == "bing":
    sQuery = "https://www.bing.com/search?&q=" + urllib.parse.quote(aArguments.q)
elif aArguments.e == "yahoo":
    sQuery = "https://search.yahoo.com/search?n=100&p=" + urllib.parse.quote(aArguments.q)
'''

try:
    fInputFile = open(sInputFile, 'r')
    lInputFile = fInputFile.readlines()
except:
    print(sInputFile + " not found...")
    exit(2)

iFirst = 0
iCount = 0
iUrls = 0
dQuery = {}
for sInputFileLine in lInputFile:
    iCount += 1
    sInputFileLine = sInputFileLine.strip()
    if iFirst == 0:
        dQuery[iUrls] = ""
        dQuery[iUrls] += sQuery + " " + sSite + sInputFileLine
    else:
        dQuery[iUrls] += "+OR+" + sSite + sInputFileLine

    if iFirst == 0: iFirst = 1

    if iCount % iNewUrlAfter == 0:
        iUrls += 1
        iFirst = 0

for sSingleQuery in dQuery.values():
    webbrowser.open(sSingleQuery)
