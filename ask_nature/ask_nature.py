import time
import unidecode
import pandas as pd

# Web Scraping Tools
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class scraper():

    def __init__(self):
        self.__start_driver()
    
    def __start_driver(self):

        #Selenium options
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--incognito")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-dev-shm-usage")

        # Starting Driver
        driver = webdriver.Chrome("drivers/chromedriver.exe")
        driver.get("https://asknature.org/")
        time.sleep(3.5)
