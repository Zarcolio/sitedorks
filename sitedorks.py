#!/usr/bin/env python3

import argparse
import urllib.parse
import webbrowser

sArgParser=argparse.ArgumentParser(description='Search Google for a search term with different websites. Use escaped quotes when necessary: \\\"')
sArgParser.add_argument('-cat', metavar="<category>", help='Choose from 1 or more categories (cloud, code, docs, other). Defaults to all categories.')
sArgParser.add_argument('-count', metavar="<count>", help='How many websites checked per query. Google has a maximum length for queries.')
sArgParser.add_argument('-engine', metavar="<engine>", help='Search with \'google\' or \'bing\', defaults to \'google\'.', choices=['bing', 'google', 'yahoo'], default="google")
sArgParser.add_argument('-file', metavar="<file>", help='Enter a custom website list.')
sArgParser.add_argument('-status', metavar="<status>",help='Enable or disable the \'site:\' operator, defaults to \'enable\'.',default='enable', choices=['enable', 'disable'])
sArgParser.add_argument('-query', metavar="<query>",  help='Enter a search term.')
aArguments=sArgParser.parse_args()

if not aArguments.query:
    sQuery = ""
else:
    sQuery = urllib.parse.quote(aArguments.query)

if aArguments.count:
    iNewUrlAfter = int(aArguments.count)
else:
    iNewUrlAfter = 30

if aArguments.file:
    sInputFile = aArguments.file
else:
    sInputFile = "domaindorks.txt"

if aArguments.status == "enable":
    sSite = "site:"
    sQuote = ""
else:
    sSite = ""
    sQuote = "%22"

sQuery = "https://www.google.com/search?num=100&filter=0&q=" + sQuery
sEndQuery = ")"

if aArguments.engine == "google":
    sQuery = "https://www.google.com/search?num=100&filter=0&q=" + urllib.parse.quote(aArguments.query) + "+AND+("
elif aArguments.engine == "bing":
    sQuery = "https://www.bing.com/search?&q=" + urllib.parse.quote(aArguments.query) + "+AND+("
elif aArguments.engine == "yahoo":
    sQuery = "https://search.yahoo.com/search?n=100&p=" + urllib.parse.quote(aArguments.query) + "+AND+("

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
iLines = len(lInputFile)

for sInputFileLine in lInputFile:
    iCount += 1
    sInputFileLine = sInputFileLine.strip()
    if iFirst == 0:
        dQuery[iUrls] = ""
        dQuery[iUrls] += sQuery + "+" + sSite + sQuote + sInputFileLine + sQuote

    else:
        dQuery[iUrls] += "+OR+" + sSite + sQuote + sInputFileLine + sQuote

    if iFirst == 0: iFirst = 1


    if iCount % iNewUrlAfter == 0 or iCount == iLines:
        dQuery[iUrls] += sEndQuery

    if iCount % iNewUrlAfter == 0:
        iUrls += 1
        iFirst = 0

for sSingleQuery in dQuery.values():
    webbrowser.open(sSingleQuery)
