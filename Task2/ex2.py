from bs4 import BeautifulSoup
from bs4.element import Comment
from selenium import webdriver
import re
import tldextract


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    var = []
    for element in texts:
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            continue
        if isinstance(element, Comment):
            continue
        else:
            var.append(element.strip())

    value = ','.join(str(x) for x in var)

    text = re.sub("[^a-zA-Z]+", " ",value)
    print(text)

def main():
    driver =  webdriver.Firefox()
    driver.maximize_window()
    link = 'https://www.accuweather.com/en/in/india-weather'
    #info = tldextract.extract(link)
    #domain_name = info.domain
    driver.get(link)
    driver.implicitly_wait(12)
    html = driver.page_source
    scrape_data = text_from_html(html)
    #split_scraped_data(scrape_data,domain_name)
    driver.quit()
    print('-------Success-------')

if __name__ == "__main__":
    main()