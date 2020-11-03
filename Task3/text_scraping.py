from bs4 import BeautifulSoup
from bs4.element import Comment
from selenium import webdriver
import re

def extract(source):

    soup = BeautifulSoup(source, 'html.parser')
    text_file = open('abc.txt', 'w')
    text_file.write(str(soup))
    text_file.close()
    DimensionsType=soup.find_element_by_xpath('//*[@id="home"]//wego-proposition//div/div[1]/i')
    print(DimensionsType)

    
url = 'https://www.wego.co.in/' 

# driver = webdriver.Firefox()

# driver.maximize_window()
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

driver.get(url)

driver.implicitly_wait(12) 

html = driver.page_source 
#print(html)  

driver.quit() 
var = extract(html)
#print(var)

