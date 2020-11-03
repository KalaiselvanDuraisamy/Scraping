import os
from bs4 import BeautifulSoup
from bs4.element import Comment
from selenium import webdriver
import re
import tldextract

def write_data(url,scrape_data,name):
    folder = os.path.splitext(url)[0]
    test_links = open(folder+"/"+name+".txt", 'w')
    test_links.write(scrape_data.lower())

def text_from_html(body):
    temp = []
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    
    for element in texts:
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            continue
        if isinstance(element, Comment):
            continue
        else:
            temp.append(element.strip())

    value = ','.join(str(x) for x in temp)
    text = re.sub("[^a-zA-Z]+", " ",value)
    
    return text

def main():
    driver =  webdriver.Firefox()
    driver.maximize_window()

    files = os.listdir('Input_Files/')
    
    for url in files:
        test_links = open('Input_Files/'+url,'r')
        input_links = test_links.readlines()
        for link in input_links:
            info = tldextract.extract(link)
            name = info.domain
            driver.get(link)
            driver.implicitly_wait(15)
            html = driver.page_source 
            scrape_data = text_from_html(html)
            write_data(url,scrape_data, name)
    driver.quit()
    print("------Finish------")

if __name__ == "__main__":
    main()