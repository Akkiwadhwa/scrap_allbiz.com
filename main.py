import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests

url = "https://allpeople.com/l/alabama-us/A%20N-A.%20A.%20Loeb/71eef4b8711a6402099cecc08b47db8e2976ca9b/"
driver = uc.Chrome()
driver.get(url)
# driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
# driver.get(url)
time.sleep(10)
print(driver.page_source)
