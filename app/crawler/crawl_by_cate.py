import time

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from .url import domain, site_map

opts = FirefoxOptions()
opts.add_argument("--headless")
# browser = webdriver.Firefox(options=opts)
browser = webdriver.Firefox()

def crawl_page_number(cate):
    browser.get(cate.link)
    page = browser.find_elements(By.CLASS_NAME,"re__pagination-number")
    return int(page[-1].text)

def crawl_cate(cate):
    links = []
    # page_number = crawl_page_number(cate)
    page_number = 3
    browser.get(cate.link)
    # for i in range(1,page_number,1):
    lists = browser.find_elements(By.CLASS_NAME,"js__product-link-for-product-id")
    for j in lists:
        links.append(j.get_attribute("href"))
    buttons = browser.find_elements(By.CLASS_NAME,"re__pagination-icon")
    print(len(buttons))
    buttons[-1].click()
    return links





