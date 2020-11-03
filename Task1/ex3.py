from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import re 
#import pandas as pd
url='https://talosintelligence.com/reputation_center/email_rep#top-senders-ip'
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)

Dimensions_Type=[]
#Dimention_Size=[]
elements=WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="sender-by-ip"]/tbody')))
#df=pd.DataFrame({"DimensionSize":Dimention_Size,"DimensionType":Dimensions_Type})
#html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[3]/div[1]/div[2]/div[2]/table/tbody
#df=pd.DataFrame({"DimensionType":Dimensions_Type})
#print(DimensionsType)
#print(type(DimensionsType))
#print(Dimention_Size)
#print(type(elements))
for ele in elements:
  #if "placeholder" not in ele.get_attribute("class"):
    for j in range(1,100):
      i = str(j)
      DimensionsType=ele.find_element_by_xpath("//*[@id='sender-by-ip']/tbody/tr["+i+"]/td[1]/a").get_attribute("textContent")
      Dimensions_Type.append(DimensionsType)
print(Dimensions_Type)
#print(len(Dimensions_Type))
