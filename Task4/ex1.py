import os
from bs4 import BeautifulSoup
from bs4.element import Comment
from selenium import webdriver
import re
import tldextract

def main():
    driver =  webdriver.Firefox()
    driver.maximize_window()

    files = os.listdir('Input_Files/')
    
    for url in files:
        test_links = open('Input_Files/'+url,'r')
        input_links = test_links.readlines()
        print(len(input_links))
        #scrape_data, name = inputs(input_links,driver)
        #write_data(url,scrape_data, name)
    print("------Finish------")

if __name__ == "__main__":
    main()