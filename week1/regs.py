import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?:twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(matches.groups())

#https://www.twitter.com/abradabba