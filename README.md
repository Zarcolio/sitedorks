# About sitedorks
Search Google or Bing for a search term with different websites. A default list is already provided, which contains Github, Gitlab, Trello etc. Also a list available with googledorks for communication invites like WhatsApp, Skype and Zoom. Currently, a list of 74 dorkable site is available.

# Why sitedorks?
Why wouldn't you just enter dorks for several websites manually? This script has a few useful functions:
* It's really easy to query different search engines.
* Dorks can be executed per 1 or more categories.
* It's easy to create different input files for different uses.
* Adding new websites to your search query can be arranged by just adding them to an input file.
* Google and Yandex ignore too many keywords/characters in a query and with argument -c it's easy to split your dork into more queries.

# Install
Sitedork should be able to run with a default Kali Linux installation without installing additional Python packages. If you're running into trouble running grepaddr, please drop me an issue and I'll try to fix it :)

# Usage
```
usage: sitedorks [-h] [-cat <category>] [-count <count>] [-engine <engine>] [-file <file>] [-site <status>]
-query <query>

Search Google for a search term with different websites. Use escaped quotes when necessary: \"

optional arguments:
  -h, --help        show this help message and exit
  -cat <category>   Choose from 1 or more categories (cloud, code, comm, docs, other), use , as delimiter. 
                    Defaults to all categories.
  -count <count>    How many websites checked per query. Google has a maximum length for queries.
  -engine <engine>  Search with 'google', 'bing', 'yahoo' or 'yandex', defaults to 'google'.
  -file <file>      Enter a custom website list.
  -site <status>    Turn the 'site:' operator 'on' or 'off', defaults to 'on'.
  -query <query>    Enter a mandatory search term.

```
# Examples
Want to look for "uber.com" with different sites containing all kinds of content? Use the following command:
```
sitedorks -query \"uber.com\"
```
Want to search for communication invites with yandex? Use the following command:
```
sitedorks -cat comm -site disable -count 10 -engine yandex -query uber
```
# Contribute?
Do you have some usefull additions to the script or to the list of dorkable websites, please send in a pull request to help make this script better :)
