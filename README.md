# About sitedorks
Search Google, Bing, Ecosia, Yahoo or Yandex for a search term with several websites. A [default list](https://github.com/Zarcolio/sitedorks/blob/master/sitedorks.csv) is already provided, which contains Github, Gitlab, Surveymonkey, Trello etc etc. Currently, a default list of 38 dorkable websites is available.
By default, the following categories are on file: 

* analysis(12)
* cloud(49)
* comm(39)
* dev(62)
* docs(48)
* edu(6)
* fin(7)
* forms(12)
* orgs(30)
* other(6)
* remote(1)
* shortener(31)
* social(76)
* storage(9)

# Why use sitedorks?
Why wouldn't you just enter dorks for several websites manually? Because:
* It's really easy to query different search engines.
* Dorks can be executed per 1 or more categories.
* It's easy to create different input files for different uses.
* Adding new websites to your search query can be arranged by just adding them to an input file.
* It already has a lot of dorkable websites included.
* The list with dorkable websites is updated regularly.
* Some search engines ignore too many keywords/characters in a query and with argument -count it's easy to split your dork into more queries.
* It contains a list of several bug bounty platforms. With 1 command you can search domains of programs on several bug bounty platforms. Find the "easter egg" in this feature :)
* It contains a list of Dutch government agencies and educational services. With 1 command you can search domains either of the Dutch government or educational services.
  * *Need help here for other lists that can be useful, for example domains of government and educational services in other countries.*
* Because you want to help plant more trees using the search engine [Ecosia](https://www.ecosia.org) (Bing based)

# Install
Sitedorks should be able to run with a default Kali Linux installation using Python 3 without installing additional Python packages.
Just run:
```
git clone https://github.com/Zarcolio/sitedorks
cd sitedorks
bash install.sh
```
If you're running into trouble running sitedorks, please drop me an issue and I'll try to fix it :)

# Usage
```
usage: sitedorks [-h] [-cat <category>] [-cats] [-count <count>] [-engine <engine>] [-file <file>]
[-query <query>] [-site <on|off|inurl>] [-excl <domains>] [-echo]

Use your favorite search engine to search for a search term with different websites. Use single quotes around a
query with double quotes. Be sure to enclose a query with single quotes it contains shell control characters like
space, ';', '>', '|', etc.

optional arguments:
  -h, --help            Show this help message, print categories on file (add -file to check other CSV file) and exit.
  -cat <category>       Choose from 1 or more categories, use ',' (comma) as delimiter. Defaults to all categories.
  -cats                 Show all categories on file, use with or without -file.
  -count <count>        How many websites are searched per query. Google has a maximum length for queries.
  -engine <engine>      Search with 'google', 'baidu', 'bing', 'bing-ecosia', 'duckduckgo' 'yahoo' or 'yandex', defaults to 
                        'google'.
  -file <file>          Enter a custom website list.
  -query <query>        Enter a mandatory search term.
  -site <on|off|inurl>  Turn the 'site:' operator 'on' or 'off', or replace it with 'inurl:' (only for Google), defaults to 
                        'on'.
  -excl <domains>       Excluded these domains from the search query.
  -echo                 Prints the search query URLs, for further use like piping or bookmarking.
  -ubb                  Updates bug bounty files (in en out scope) and exits. Uses bbrecon.
  -wait <seconds>       Wait x seconds, defaults to 5 seconds.
```

# Examples
Small warning here: if you don't use **-cat** sitedorks will open a lot of tabs in your browser and probably will make Google throw you a CAPTCHA. Increase waiting time with option '-wait' to decrease the chance of getting a CAPTCHA.

Want to look for "uber.com" with different sites containing all kinds of content using Google? Use the following command:
```
sitedorks -query '"uber.com"'
```
Want to look for "uber website" (with quotes and spaces in the query)? Use the following command:
```
sitedorks -query '"uber website"'
```
Want to search for communication invites with Yandex but leave site: out of the query? Just use the following command:
```
sitedorks -cat comm -site disable -engine yandex -query uber
```
And if you  want to see which categories are on file, for example with the [hackerone](https://www.hackerone.com) platform:
```
sitedorks -file sitedorks-bbrecon.csv -cats
```
If you want to download/update the bug bounty files, you can use the -ubb parameter (it uses [bbrecon](https://github.com/serain/bbrecon)):
```
sitedorks -ubb
```
The -ubb argument creates two files: sitedorks-bbrecon-inscope.csv and sitedorks-bbrecon-outscope.csv.
Use the following command for finding exploitable systems or juicy info (always check if a system is in scope, although these these domains are in scope, it doesn't always mean that this subdomain or system is):
```
sitedorks -file sitedorks-bbrecon-inscope.csv -cat somevdp -query "exploitable systems/juicy info"
```
Use this command for finding juicy info only, because these domains are out of scope:
```
sitedorks -file sitedorks-bbrecon-outscope.csv -cat somevdp -query "juicy info"
```

# Google Dorks
Don't know what to look for? 
Try:
* https://twitter.com/hashtag/googledork%20OR%20%23googledorks
* https://gbhackers.com/latest-google-dorks-list

# Contribute?
Do you have some usefull additions to the script or to the list of dorkable websites, please send in a pull request to help make this script better or contact me @ [Twitter](https://twitter.com/zarcolio) :)
