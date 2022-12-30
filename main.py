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
time.sleep(10)
soup = BeautifulSoup(driver.page_source, "html.parser")
data = soup.select("div.res-info div:nth-child(2)")
time.sleep(10)
driver.get("https://www.allbiz.com/")
time.sleep(10)
for i in data:
    name = i.text
    res = name[name.find(" at ") + len(" at "):]
    a = res.strip()
    driver.get(f"https://www.allbiz.com/search?ss={a}&ia=US_AL")
    s = driver.find_element(By.CLASS_NAME,"result-b").find_elements(By.TAG_NAME,"a")
    for link in s:
        link1 = link.get_attribute("href")
        driver.get(link1)
        try:
            name = driver.find_element(By.CLASS_NAME,"focus-p").text.strip()
            category = driver.find_element(By.CLASS_NAME,"inline-block").find_element(By.TAG_NAME,"span").text.strip()
            address = driver.find_element(By.CLASS_NAME,"inline").text.replace(f" {name} Get Directions"," ").strip()
        except:
            pass
        else:
            print(name)
            print(address)
            print(category)

