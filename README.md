# About sitedork
Search Google for a search term with different websites. A default list is already provided.

# Install
Sitedork should be able to run with a default Kali Linux installation without installing additional Python packages. If you're running into trouble running grepaddr, please drop me an issue and I'll try to fix it :)

# Usage
```
usage: sitedorks.py [-h] [-c <count>] [-f <file>] -q <query>

Search Google for a search term with different websites. Use escaped quotes when necessary: \"

optional arguments:
  -h, --help  show this help message and exit
  -c <count>  How many websites checked per query. Google has a maximum length for queries.
  -f <file>   Enter a custom website list.
  -q <query>  Enter a search term.
```
# Examples
```
sitedorks -q \"uber.com\"
```
