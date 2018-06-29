#!/usr/bin/python3

## One parameter - URL of instagram post

from sys import argv
import urllib.request
from bs4 import BeautifulSoup
import os

script, website = argv

socks = urllib.request.urlopen(str(website))
OriginPage = socks.read()  # Originpage = HTML script dump
socks.close()

soup = BeautifulSoup(OriginPage, "html.parser")   # soup = formatted HTML script


# Filter URLs of images
URLs = []

for link in soup.find_all('meta'):
    URLs.append(link.get('content'))

Pictures = []

for i in URLs:
    if i and 'n.jpg' in i:          # PARAMETER 2
        Pictures.append(i)


# Make folder for incoming image

directories = os.path.dirname('images/')
for i in directories:
    if not os.path.isdir('images/'):
        os.makedirs('images/')

# Save image into folder

for i in Pictures:
    filename = i.split('/')[-1]
    try:
        urllib.request.urlretrieve(i, 'images/' + filename)
        print(filename)      # print on each successful picture download
    except:
        print('img not found')
        
print('Download Complete.')
