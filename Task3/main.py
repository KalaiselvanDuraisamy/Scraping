from bs4 import BeautifulSoup
from bs4.element import Comment
from selenium import webdriver
import re
import tldextract

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

def split_scraped_data(scrape_data,domain_name):
    text_file = open(domain_name+'.txt', 'w')
    text_file.write(scrape_data.lower())
    text_file.close()
    
def main():
    test_links = open('travel_url.txt', 'r') 
    url = test_links.readlines()
    driver =  webdriver.Firefox()
    driver.maximize_window()
    
    for link in url:
        info = tldextract.extract(link)
        driver.get(link)
        driver.implicitly_wait(15)
        html = driver.page_source 
        scrape_data = text_from_html(html)
        split_scraped_data(scrape_data,info.domain)
    
    driver.quit()
    print('-------Success-------')

if __name__ == "__main__":
    main()