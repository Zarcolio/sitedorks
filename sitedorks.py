#!/usr/bin/env python3

import argparse
import urllib.parse
import webbrowser

sArgParser=argparse.ArgumentParser(description='Search Google for a search term with different websites. Use escaped quotes when necessary: \\\"')
sArgParser.add_argument('-cat', metavar="<category>", help='Choose from 1 or more categories (cloud, code, comm, docs, other), use , as delimiter. Defaults to all categories.')
sArgParser.add_argument('-count', metavar="<count>", help='How many websites checked per query. Google has a maximum length for queries.')
sArgParser.add_argument('-engine', metavar="<engine>", help='Search with \'google\', \'bing\', \'yahoo\' or \'yandex\', defaults to \'google\'.', choices=['bing', 'google', 'yahoo', 'yandex'], default="google")
sArgParser.add_argument('-file', metavar="<file>", help='Enter a custom website list.')
sArgParser.add_argument('-site', metavar="<status>",help='Turn the \'site:\' operator \'on\' or \'off\', defaults to \'on\'.',default='on', choices=['on', 'off'])
sArgParser.add_argument('-query', metavar="<query>",  help='Enter a mandatory search term.', required=True)
aArguments=sArgParser.parse_args()

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
    sInputFile = "domaindorks.csv"

if aArguments.site == "on":
    sSite = "site:"
    sQuote = ""
else:
    sSite = ""
    sQuote = "%22"

if aArguments.cat: lCategory = aArguments.cat.split(",")

sQuery = "https://www.google.com/search?num=100&filter=0&q=" + sQuery
sEndQuery = ")"

if aArguments.engine == "google":
    sQuery = "https://www.google.com/search?num=100&filter=0&q=" + urllib.parse.quote(aArguments.query) + "+AND+("
elif aArguments.engine == "bing":
    sQuery = "https://www.bing.com/search?&q=" + urllib.parse.quote(aArguments.query) + "+AND+("
elif aArguments.engine == "yandex":
    sQuery = "https://yandex.com/search/?text=" + urllib.parse.quote(aArguments.query) + "+AND+("
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


    sInputFileLine = sInputFileLine.strip()
    lInputFileLineCsv = sInputFileLine.split(";")

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
