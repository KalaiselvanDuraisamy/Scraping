from urllib.request import urlopen
import zipfile
from zipfile import ZipFile
import os
from selenium import webdriver
import re

zipcontent = urlopen('http://www.stopforumspam.com/downloads/listed_ip_1_ipv6.zip').read()

with open("url_links", 'wb') as f:
   f.write(zipcontent)
directory_to_extract_to = '/home/test2/Desktop/Kalai/Scarping/results'
path_to_zip_file = '/home/test2/Desktop/Kalai/Scarping/url_links'
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)

entries = os.listdir(directory_to_extract_to)
test_links = open(directory_to_extract_to+'/'+ entries[0], 'r') 
url = test_links.readlines()
print(type(url))
content = str(url)
ipv4_pattern = re.compile(r'(?:^|\b(?<!\.))(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])') 
ipv4_list = ipv4_pattern.findall(content)
print(len(ipv4_list))        
