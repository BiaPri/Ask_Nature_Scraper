import os
import time
import pandas as pd

# Web Scraping Tools
from bs4 import BeautifulSoup
from selenium import webdriver

class scraper():

    def __init__(self):
        self.__start_driver()
    
    def __start_driver(self):

        #Selenium options
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--incognito")
        options.add_argument("--headless")
        options.add_argument("--disable-popup-blocking")

        # Starting Driver
        dir = os.path.dirname(__file__)
        location = os.path.join(dir, "drivers", "chromedriver.exe")
        driver = webdriver.Chrome(location)
        driver.maximize_window()
        driver.get("https://asknature.org/")
        time.sleep(2)

        self.__driver = driver

    def home_page_click(self, search):
        try:
            elem = self.__driver.find_element_by_xpath(f'//a[@data-title = "{search}"]')
            elem.click()
        except:
            print("This element is not present on the website")
            
    def collect_data(self, number):
        titles = []
        dico = {}

        html_doc = self.__driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')
        soup

        for elem in soup.find_all('h4', class_='widont')[4:]:
            titles.append(elem.text)

        for i in range(number):
            elem = self.__driver.find_elements_by_xpath('//div[@class="preview-text over-image"]')[i]
            elem.click()
            time.sleep(2)
            
            html_doc = self.__driver.page_source
            soup = BeautifulSoup(html_doc, 'html.parser')
            para = []
            for elem in soup.find_all('p'):
                para.append(elem.text)
                
            full_text = "\n\n".join(para)
            dico[titles[i]] = full_text

            self.__driver.back()
            time.sleep(2)
        return dico 

if __name__ == "__main__":
    srape = scraper()
    srape.home_page_click("Biological Strategies")
    print(srape.collect_data(3))
