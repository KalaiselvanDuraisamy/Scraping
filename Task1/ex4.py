from bs4 import BeautifulSoup
from selenium import webdriver
import re 
from selenium.webdriver.common.by import By

url='https://talosintelligence.com/reputation_center/email_rep#top-senders-ip'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

html = driver.page_source
Dimensions_Type=[]
review_SeeMore = driver.find_elements_by_xpath('//*[@id="sender-by-ip"]/tbody')
print(review_SeeMore)
for review in review_SeeMore:
        #for paragraph in review.find_elements(By.TAG_NAME, "p"):
        #    print(paragraph.get_attribute('textContent').encode("utf-8"))
        #print('\n============================\n')
    for j in range(1,50):
        i = str(j)
        DimensionsType=review.find_element_by_xpath("//*[@id='sender-by-ip']/tbody/tr["+i+"]/td[1]/a").get_attribute("textContent")
        Dimensions_Type.append(DimensionsType)
#print(Dimensions_Type)
#print(len(Dimensions_Type))