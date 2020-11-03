import re 
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
import zipfile
from zipfile import ZipFile
import os

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
test_links = open('links.txt', 'r') 
url = test_links.readlines()
file1 = open('results.txt', 'w') 

valid_ip_list = []
ip_value = []
value1 = ''
ipv4_pattern = re.compile(r'(?:^|\b(?<!\.))(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])') 
ipv6_pattern = re.compile(r'((([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])))')

def function_one(link):
    zip_content = urlopen(link).read()
    with open("url_links", 'wb') as f:
        f.write(zip_content)
        directory_to_extract_to = '/home/test2/Desktop/Kalai/Scarping'
        path_to_zip = '/home/test2/Desktop/Kalai/Scarping/url_links'  
    with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
        zip_content = os.listdir(directory_to_extract_to)
        test_links = open(directory_to_extract_to+'/'+ zip_content[0], 'r') 
        url1 = test_links.readlines()
        content = str(url1)
        ipv_4 = ipv4_pattern.findall(content)
    def check_ip(pattern,Ip):  
        if(re.search(pattern, Ip)):  
            return True           
        else:  
            return False 
    for line in range(len(ipv_4)):
        val1 = check_ip(ipv4_pattern,ipv_4[line])
        if val1:
            valid_ip_list.append(ipv_4[line])

        
def function_two(html):
    soup = BeautifulSoup(html, 'html.parser')
    var = soup.findAll('td',{'class':'sorted-by min-150'})
    if var:
        ip_links = [] 
        category = []
        for link in soup.findAll('td',{'class':'sorted-by min-150'}):
            ipv4_links = link.get("class", ""), link.text
            ip_links.append(ipv4_links[1])

        for link in soup.findAll('td',{'class':'no_country_lookup min-100 rep_email'}):
            ipv4_category = link.get("class", ""), link.text
            category.append(ipv4_category[1])

        j = 0
        for i in category:
            if i == 'Poor':
                valid_ip_list.append(ip_links[j])
            j+=1
    else:

        ipv4_list = ipv4_pattern.findall(html) 
        ipv6_list = ipv6_pattern.findall(html)      
        def check(pattern,Ip):  
            if(re.search(pattern, Ip)):  
                return True           
            else:  
                return False 

        if ipv4_list or ipv6_list:
            for line in range(len(ipv4_list)):
                val1 = check(ipv4_pattern,ipv4_list[line])
                if val1:
                    valid_ip_list.append(ipv4_list[line])

for link in url:
    driver.get(link)
    html = driver.page_source
    if value1 == html:
        function_one(link)
    else:
        function_two(html)
    value1 = html
 
for i in valid_ip_list: 
    if i not in ip_value: 
        ip_value.append(i)
        file1.writelines(i) 
        file1.writelines("\n")


valid_ip_list.clear()
ip_value.clear()           
file1.close()
driver.quit()
print("Success...")

