#!/usr/bin/env python3

import argparse
import urllib.parse
import webbrowser
import sys
import os

sArgParser=argparse.ArgumentParser(description="Search Google for a search term with different websites. Use escaped quotes when search for an exact search term: \\\". Be sure to enclose a query with double quotes it contains shell control characters like space, ';', '>', '|', etc.")
sArgParser.add_argument('-cat', metavar="<category>", help='Choose from 1 or more categories (careers, cloud, code, edu, comm, docs, forms, social, other), use \',\' (comma) as delimiter. Defaults to all categories.')
sArgParser.add_argument('-count', metavar="<count>", help='How many websites checked per query. Google has a maximum length for queries.')
sArgParser.add_argument('-engine', metavar="<engine>", help='Search with \'google\', \'bing\', \'duckduckgo\' \'yahoo\' or \'yandex\', defaults to \'google\'.', choices=['bing', 'duckduckgo', 'google', 'yahoo', 'yandex'], default="google")
sArgParser.add_argument('-file', metavar="<file>", help='Enter a custom website list.')
sArgParser.add_argument('-query', metavar="<query>",  help='Enter a mandatory search term.', required=True)
sArgParser.add_argument('-site', metavar="<status>",help='Turn the \'site:\' operator \'on\' or \'off\', or replace it with \'inurl\' (only for Google), defaults to \'on\'.',default='on', choices=['on', 'off', 'inurl'])
sArgParser.add_argument('-excl', metavar="<domains>",  help='Excluded these domains from the search query.')

aArguments=sArgParser.parse_args()

if aArguments.site == "inurl" and aArguments.engine != "google":
    print("inurl: only works with Google.")
    print()
    sArgParser.print_help()
    sys.exit(2)


if not aArguments.query:
    sQuery = ""
else:
    sQuery = urllib.parse.quote(aArguments.query)

if aArguments.count:
    iNewUrlAfter = int(aArguments.count)
else:
    iNewUrlAfter = 15

if aArguments.file:
    sInputFile = aArguments.file
else:
    sInputFile = os.path.dirname(os.path.realpath(sys.argv[0])) + "/sitedorks.csv"

if aArguments.site == "on":
    sSite = "site:"
    sQuote = ""
elif aArguments.site == "inurl":
    sSite = "inurl:"
    sQuote = ""
else:
    sSite = ""
    sQuote = "%22"

if aArguments.cat:
    lCategory = aArguments.cat.split(",")

if aArguments.excl:
    lExcludeDomains = aArguments.excl.split(",")

if aArguments.engine == "google":
    if aArguments.site == "inurl":
        sInurl = "inurl:"
    else:
        sInurl = ""
    sQuery = "https://www.google.com/search?num=100&filter=0&q=(" + sInurl + urllib.parse.quote(aArguments.query) + ")+AND+("
elif aArguments.engine == "bing":
    sQuery = "https://www.bing.com/search?&q=(" + urllib.parse.quote(aArguments.query) + ")+AND+("
elif aArguments.engine == "duckduckgo":
    sQuery = "https://duckduckgo.com/?q=(" + urllib.parse.quote(aArguments.query) + ")+AND+("
elif aArguments.engine == "yandex":
    sQuery = "https://yandex.com/search/?text=(" + urllib.parse.quote(aArguments.query) + ")+AND+("
elif aArguments.engine == "yahoo":
    sQuery = "https://search.yahoo.com/search?n=100&p=(" + urllib.parse.quote(aArguments.query) + ")+AND+("

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

if aArguments.cat:
    iLines = sum(1 for s in lInputFile if "," + aArguments.cat in s)
    if iLines == 0:
        print("Category '" + aArguments.cat + "' not found, exiting...")
        exit(2)
else:
    iLines = len(open(sInputFile).readlines())

sEndQuery = ")"

for sInputFileLine in lInputFile:


    sInputFileLine = sInputFileLine.strip()
    lInputFileLineCsv = sInputFileLine.split(",")

    if aArguments.excl:
        if lInputFileLineCsv[0] in lExcludeDomains:
            continue

    try:
        if aArguments.cat and lInputFileLineCsv[1] not in lCategory:
            continue
    except:
        print("Error in CSV file")

    iCount += 1
    if iFirst == 0:
        dQuery[iUrls] = ""
        dQuery[iUrls] += sQuery + sSite + sQuote + lInputFileLineCsv[0] + sQuote

    else:
        dQuery[iUrls] += "+|+" + sSite + sQuote + lInputFileLineCsv[0] + sQuote

    if iFirst == 0: iFirst = 1

    if iCount % iNewUrlAfter == 0 or iCount == iLines:
        dQuery[iUrls] += sEndQuery

    if iCount % iNewUrlAfter == 0:
        iUrls += 1
        iFirst = 0

for sSingleQuery in dQuery.values():
    webbrowser.open(sSingleQuery)