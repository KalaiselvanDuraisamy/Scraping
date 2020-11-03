from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from selenium import webdriver
import re
import tldextract

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def split_data(split_scrape_data):
    data = list(filter(lambda ele: re.search("[a-zA-Z\s]+", ele) is not None, split_scrape_data))
    data_list = []
    for j in range(len(data)):
        data_list.append(''.join(i for i in data[j] if i.isalnum()))
    return data_list 

def split_scraped_data(scrape_data,domain_name):
    split_scrape_data = scrape_data.split(" ")
    
    data_list = split_data(split_scrape_data)
    
    text_page = open(domain_name+'.txt', 'w')

    for i in range(len(data_list)):
        text_page.write(data_list[i])
        text_page.write("\t")
    print("Success...")
def scrape():
    test_links = open('input_url.txt', 'r') 
    url = test_links.readlines()
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    for link in url:
        info = tldextract.extract(link)
        domain_name = info.domain
        driver.get(link)
        var = driver.page_source
        #link = 'https://www.accuweather.com/en/in/india-weather'
        #driver.get(link)
        #var = driver.page_source
        html = bytes(var, 'utf-8') 
        scrape_data = text_from_html(html)
        split_scraped_data(scrape_data,domain_name)
  
def main():
    scrape()

if __name__ == "__main__":
    main()