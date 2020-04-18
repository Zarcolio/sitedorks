#!/usr/bin/env python3

import argparse
import urllib.parse
import webbrowser

sArgParser=argparse.ArgumentParser(description='Search Google for a search term with different websites. Use escaped quotes when necessary: \\\"')
sArgParser.add_argument('-q', help='Enter a search term.', required=True)
sArgParser.add_argument('-f', help='Enter a custom website list.')
aArguments=sArgParser.parse_args()

if aArguments.f:
    sInputFile = aArguments.f
else:
    sInputFile = "zorks-domains.txt"

sQuery = "https://www.google.nl/search?num=100&filter=0&q=" + urllib.parse.quote(aArguments.q)

try:
    fInputFile = open(sInputFile, 'r')
    lInputFile = fInputFile.readlines()
except:
    print(sInputFile + " not found...")
    exit(2)


iNewPageAfter = 30
iFirst = 0
iCount = 0
iPage = 0
dQuery = {}
for sInputFileLine in lInputFile:
    iCount += 1
    sInputFileLine = sInputFileLine.strip()
    if iFirst == 0:
        dQuery[iPage] = ""
        dQuery[iPage] += sQuery+ "+site:" + sInputFileLine
    else:
        dQuery[iPage] += "+|" + "site:" + sInputFileLine

    if iFirst == 0: iFirst = 1

    if iCount % iNewPageAfter == 0:
        iPage += 1
        iFirst = 0

for sSingleQuery in dQuery.values():
    webbrowser.open(sSingleQuery)
