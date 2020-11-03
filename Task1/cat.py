from bs4 import BeautifulSoup
from selenium import webdriver
import re 
url='https://talosintelligence.com/reputation_center/email_rep#top-senders-ip'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

data = driver.page_source

ip_links = [] 
soup = BeautifulSoup(data, 'html.parser')
for link in soup.findAll('td',{'class':'sorted-by min-150'}):
    ipv4_links = link.get("class", ""), link.text
    ip_links.append(ipv4_links[1])

category = []
for link in soup.findAll('td',{'class':'no_country_lookup min-100 rep_email'}):
    ipv4_category = link.get("class", ""), link.text
    category.append(ipv4_category[1])

print(category)
j = 0
file1 = open('results.txt', 'w')
for i in category:
    if i == 'Poor':
        #print("hai"+i)
        file1.writelines(ip_links[j]) 
        file1.writelines("\n")
    j+=1
file1.close()
print("Success...")
