#!/usr/bin/env python3

import argparse
import urllib.parse
import webbrowser
import sys
import os

def GetCat():
    dCatCounty = {}
    for sLine in lInputFile:
        sLine = sLine.strip()
        lLine = sLine.split(",")
        if lLine[1] in dCatCounty:
            dCatCounty[lLine[1]] = dCatCounty[lLine[1]] + 1
        else:
            dCatCounty[lLine[1]] = 1
    sCatList = ""
    for iCounter, sCat in enumerate(sorted(dCatCounty)):
        if iCounter == len(dCatCounty)-1:
            sCatList = sCatList + sCat + "(" + str(dCatCounty[sCat]) + ")."
        else:
            sCatList = sCatList + sCat + "(" + str(dCatCounty[sCat]) + "), "
            
    return sCatList

sArgParser=argparse.ArgumentParser(add_help=False, description="Use your favorite search engine to search for a search term with different websites. Use single quotes around a query with double quotes. Be sure to enclose a query with single quotes it contains shell control characters like space, ';', '>', '|', etc.")
sArgParser.add_argument('-h', '--help', help='Show this help message, print categories on file (add -file to check other CSV file) and exit.', action="store_true")
sArgParser.add_argument('-cat', metavar="<category>", help='Choose from 1 or more categories, use \',\' (comma) as delimiter. Defaults to all categories.')
sArgParser.add_argument('-cats', help='Show all categories on file, use with or without -file.', action="store_true")
sArgParser.add_argument('-count', metavar="<count>", help='How many websites are searched per query. Google has a maximum length for queries.')
sArgParser.add_argument('-engine', metavar="<engine>", help='Search with \'google\', \'baidu\', \'bing\', \'bing-ecosia\', \'duckduckgo\' \'yahoo\' or \'yandex\', defaults to \'google\'.', choices=['bing', 'bing-ecosia', 'baidu', 'duckduckgo', 'google', 'yahoo', 'yandex'], default="google")
sArgParser.add_argument('-file', metavar="<file>", help='Enter a custom website list.')
sArgParser.add_argument('-query', metavar="<query>",  help='Enter a mandatory search term.')
sArgParser.add_argument('-site', metavar="<on|off|inurl>",help='Turn the \'site:\' operator \'on\' or \'off\', or replace it with \'inurl:\' (only for Google), defaults to \'on\'.',default='on', choices=['on', 'off', 'inurl'])
sArgParser.add_argument('-excl', metavar="<domains>",  help='Excluded these domains from the search query.')
sArgParser.add_argument('-echo',  help='Prints the search query URLs, for further use like piping or bookmarking.', action="store_true")
sArgParser.add_argument('-ubb',  help='Updates bug bounty files (in en out scope) and exits. Uses bbrecon.', action="store_true")

aArguments=sArgParser.parse_args()

   
if aArguments.ubb:
    import subprocess
    import json
    from tldextract import extract
    
    #sOutput = subprocess.check_output("bbrecon get scopes --type web --output json", shell=True)
    sOutput = subprocess.check_output("bbrecon get programs --type web -o json", shell=True)
    fCsvInScope = open(os.path.dirname(os.path.realpath(sys.argv[0])) + "/sitedorks-bbrecon-inscope.csv", 'w', buffering=1)
    fCsvOutScope = open(os.path.dirname(os.path.realpath(sys.argv[0])) + "/sitedorks-bbrecon-outscope.csv", 'w', buffering=1)

    OutputJson = json.loads(sOutput)
    dDomainsInScope = {}
    dDomainsOutScope = {}
    for sLine in OutputJson:
        sLine["slug"] = sLine["slug"].lower()
        #print(sLine["in_scope"])
        #print(sLine["out_scope"])
        #print()
        for sInScope in sLine["in_scope"]:
            if sInScope["type"] == "web":
                lInScopeValues = sInScope["value"].lower().split(",")
                for sInScopeValue in lInScopeValues:
                    if sInScopeValue.endswith("amazonaws.com") or sInScopeValue.endswith("cloudfront.net") or sInScopeValue.endswith("azurefd.net") or sInScopeValue.endswith("azurewebsites.net"):
                        sDomain = sInScopeValue
                    else:
                        dl3, dl2, dl1 = extract(sInScopeValue)
                        sDomain = dl2 + "." + dl1
    
                    if " " in sDomain or "*" in sDomain or sDomain.endswith(".") or sDomain.endswith(".onion"):
                        continue
                    else:
                        dDomainsInScope[sDomain] = sLine["slug"]

        for sOutScope in sLine["out_scope"]:
            if sOutScope["type"] == "web":
                lOutScopeValues = sOutScope["value"].lower().split(",")
                for sOutScopeValue in lOutScopeValues:
                    if sOutScopeValue.endswith("amazonaws.com") or sOutScopeValue.endswith("cloudfront.net") or sOutScopeValue.endswith("azurefd.net") or sOutScopeValue.endswith("azurewebsites.net"):
                        sDomain = sOutScopeValue
                    else:
                        dl3, dl2, dl1 = extract(sOutScopeValue)
                        sDomain = dl2 + "." + dl1
    
                    if " " in sDomain or "*" in sDomain or sDomain.endswith(".") or sDomain.endswith(".onion"):
                        continue
                    else:
                        if not sDomain in dDomainsInScope:
                            dDomainsOutScope[sDomain] = sLine["slug"]

    
    for sLine in dDomainsInScope:
        fCsvInScope.write(sLine +","+ dDomainsInScope[sLine] +"\n")

    for sLine in dDomainsOutScope:
        fCsvOutScope.write(sLine +","+ dDomainsOutScope[sLine] +"\n")
    print("sitedorks-bbrecon-inscope.csv and sitedorks-bbrecon-outscope.csv have been updated.")
    exit()

sAnswer=""
if not aArguments.cat:
    while sAnswer.lower() != "y" and sAnswer.lower() != "n":
        sAnswer = input("Not providing -cat will open a lot of tabs/windows in your browser. Do you want to continue? (y/n) ")
    
    if sAnswer.lower() == "n":
        exit()


if aArguments.site == "inurl" and aArguments.engine != "google" and aArguments.engine != "duckduckgo":
    print("inurl: only works with Google and DuckDuckGo.")
    print()
    sArgParser.print_help()
    sys.exit(2)


if not aArguments.query:
    sQuery = ""
else:
    sQuery = urllib.parse.quote(aArguments.query)

if aArguments.count:
    iNewUrlAfter = int(aArguments.count)
    if aArguments.engine == "baidu":
        print("Because of limitations with Baidu, -count is lowered to 2.")
        iNewUrlAfter = 2
else:
    iNewUrlAfter = 14

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

try:
    fInputFile = open(sInputFile, 'r')
    lInputFile = fInputFile.readlines()
 
    if aArguments.cats:
        sCatList = GetCat()
        print()
        print("Current categories on file are: " + sCatList)
        print()
        exit(0)
        
    if aArguments.help:
        sCatList = GetCat()
        sArgParser.print_help()
        print()
        print("Current categories on file are: " + sCatList)
        print()
        exit(0)
    elif not aArguments.query:
        print("sitedorks: error: the following argument is required: -query")
        exit(2)
except FileNotFoundError:
    print(sInputFile + " not found...")
    exit(2)


if aArguments.engine == "google":
    sQuery = "https://www.google.com/search?num=100&filter=0&q=" + urllib.parse.quote(aArguments.query) + "+AND+("
elif aArguments.engine == "baidu":
    sQuery = "https://www.baidu.com/s?wd=" + urllib.parse.quote(aArguments.query) + "+("
elif aArguments.engine == "bing":
    sQuery = "https://www.bing.com/search?&count=100&q=" + urllib.parse.quote(aArguments.query) + "+AND+("
elif aArguments.engine == "bing-ecosia":
    sQuery = "https://www.ecosia.org/search?&q=" + urllib.parse.quote(aArguments.query) + "+AND+("
elif aArguments.engine == "duckduckgo":
    sQuery = "https://duckduckgo.com/?q=" + urllib.parse.quote(aArguments.query) + "+AND+("
elif aArguments.engine == "yandex":
    sQuery = "https://yandex.com/search/?text=" + urllib.parse.quote(aArguments.query) + "+AND+("
elif aArguments.engine == "yahoo":
    sQuery = "https://search.yahoo.com/search?n=100&p=" + urllib.parse.quote(aArguments.query) + "+AND+("


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
    if aArguments.echo:
        print(sSingleQuery)
    
    webbrowser.open(sSingleQuery)