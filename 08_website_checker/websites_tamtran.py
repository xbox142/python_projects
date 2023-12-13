import requests
import csv
from http import HTTPStatus
from fake_useragent import UserAgent

# import re
# with open('websites.csv', 'r') as f:
#     contents = f.readlines()

# pattern = re.compile('\"(.*)\"')
# websites = []

# for content in contents:
#     website = re.findall(pattern,content)
#     websites.append(website)

websites = []

with open('websites.csv', 'r') as f:
    contents = csv.reader(f)
    for row in contents:
        websites.append(f'https://{row[1]}')

ua = UserAgent()

for i in websites:
    try:   
        r = requests.get(i,headers={'User-Agent': ua.chrome})
        print(i, r.status_code)
    except Exception:
        print(f'**Could not get information for website: {i}')