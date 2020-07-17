# About sitedorks
Search Google, Bing, Yahoo or Yandex for a search term with different websites. A default list is already provided, which contains Github, Gitlab, Surveymonkey, Trello etc etc. Currently, a default list of 237 dorkable websites is available.
Current categories on file are: 
* analysis(10)
* cloud(34)
* code(38)
* comm(27)
* companies(3)
* docs(36)
* edu(2)
* forms(11)
* orgs(13)
* other(4)
* remote(1)
* shortener(15)
* social(40)
* storage(3)

# Why sitedorks?
Why wouldn't you just enter dorks for several websites manually? Because:
* It's really easy to query different search engines.
* Dorks can be executed per 1 or more categories.
* It's easy to create different input files for different uses.
* Adding new websites to your search query can be arranged by just adding them to an input file.
* It already has a lot of dorkable websites included.
* The list with dorkable websites is updated regularly.
* Some search engines ignore too many keywords/characters in a query and with argument -count it's easy to split your dork into more queries.
* It contains a list for Bugcrowd, HackerOne, Intigrity and YesWeHack. With 1 command you can search domains of programs on several bug bounty platforms :)

# Install
Sitedork should be able to run with a default Kali Linux installation without installing additional Python packages. If you're running into trouble running sitedorks, please drop me an issue and I'll try to fix it :)

# Usage
```
usage: sitedorks [-h] [-cat <category>] [-count <count>] [-engine <engine>] [-file <file>] [-query <query>]
[-site <on|off|inurl>] [-excl <domains>] [-echo]

Use your favorite search engine to search for a search term with different websites. Use single quotes around
a query with double quotes. Be sure to enclose a query with single quotes it contains shell control characters
like space or ';', '>', '|', etc.

optional arguments:
  -h, --help            Show this help message, print categories on file (add -file to check other CSV
                        file) and exit.
  -cat <category>       Choose from 1 or more categories, use ',' (comma) as delimiter. Defaults to all
                        categories.
  -count <count>        How many websites checked per query. Google has a maximum length for queries.
  -engine <engine>      Search with 'google', 'baidu', 'bing', 'duckduckgo' 'yahoo' or 'yandex', defaults
                        to 'google'.
  -file <file>          Enter a custom website list.
  -query <query>        Enter a mandatory search term.
  -site <on|off|inurl>  Turn the 'site:' operator 'on' or 'off', or replace it with 'inurl:' (only for
                        Google), defaults to 'on'.
  -excl <domains>       Excluded these domains from the search query.
  -echo                 Prints the search query URLs, for further use like piping or bookmarking.

usage: sitedorks [-h] [-cat <category>] [-count <count>] [-engine <engine>] [-file <file>] [-query <query>]
                 [-site <on|off|inurl>] [-excl <domains>] [-echo]
```

# Examples
Want to look for "uber.com" with different sites containing all kinds of content using Google? Use the following command:
```
sitedorks -query '"uber.com"'
```
Want to look for "uber website" (with quotes and spaces in the query)? Use the following command:
```
sitedorks -query '"uber website"'
```
Want to search for communication invites with yandex but leave site: out of the query? Just use the following command:
```
sitedorks -cat comm -site disable -engine yandex -query uber
```
And if you  want to see which categories are on file, for example with the [hackerone](https://www.hackerone.com) platform:
```
sitedorks -file sitedorks-hackerone.csv -cats
```
# Contribute?
Do you have some usefull additions to the script or to the list of dorkable websites, please send in a pull request to help make this script better :)
