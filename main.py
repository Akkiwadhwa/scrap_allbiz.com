import time
import pandas
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
list1=[]
li = []
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
    try:
        name = i.text
        res = name[name.find(" at ") + len(" at"):]
        a = res.strip()
        print(a)
        driver.get(f"https://www.allbiz.com/search?ss={a}&ia=US_AL")
        s = driver.find_element(By.CLASS_NAME, "result-b").find_elements(By.TAG_NAME, "a")
        for link in s:
            link1 = link.get_attribute("href")
            driver.get(link1)
            name = driver.find_element(By.CLASS_NAME, "focus-p").text.strip()
            category = driver.find_element(By.CLASS_NAME, "inline-block").find_element(By.TAG_NAME, "span").text.strip()
            address = driver.find_element(By.CLASS_NAME, "inline").text.replace(f"Get Directions", " ").strip()
            attri = driver.find_element(By.CLASS_NAME, "attributes").find_elements(By.TAG_NAME, "div")
            for i in attri:
                z = i.find_element(By.TAG_NAME, "a").text
                li.append(z)
    except:
        pass
    else:
        dict = {
            "Name": a,
            "Category": category,
            "Address": address,
            "attributes": z}
        print(dict)
        list1.append(dict)

df = pandas.DataFrame(list1)
df.to_csv("dataset.csv")
