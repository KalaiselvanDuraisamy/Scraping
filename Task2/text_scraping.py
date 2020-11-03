from bs4 import BeautifulSoup
from bs4.element import Comment
from selenium import webdriver
import re

def extract(source):

    soup = BeautifulSoup(source, 'html.parser')

    texts = soup.findAll(text=True)
    #print(texts)

    list_1 = []
    
    for i in texts:
        if i.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            continue
        if isinstance(i, Comment):
            continue
        else:
            list_1.append(i.strip()) 

    print(list_1)        

    # res = ','.join(str(x) for x in list_1)
    # print(res)

    # res_1 = re.sub('[^a-zA-Z]+', ' ', res)

    # print(res_1.lower())    
    
url = input('Enter your search here :') 
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#inary = FirefoxBinary('path/to/installed firefox binary')

driver = webdriver.Firefox()

driver.maximize_window()

driver.get(url)

driver.implicitly_wait(12) 

html = driver.page_source 
#print(html)  

driver.quit() 

print(extract(html))

