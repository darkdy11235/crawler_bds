from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from .url import domain, site_map
from ..databases.models.some_model import loai


opts = FirefoxOptions()
opts.add_argument("--headless")
# browser = webdriver.Firefox(options=opts)
browser = webdriver.Firefox()

browser.get(domain + site_map)

def crawl_cate(ul):
    result = []
    list_a = ul.find_elements(By.TAG_NAME,"a")
    for i in range(1,len(list_a)):
        r = loai(list_a[i].text, list_a[i].get_attribute("href"))
        result.append(r)
    return result
def crawl_loai_thue_loai_ban():
    ul = browser.find_elements(By.CLASS_NAME,"sitemapblock_row1")
    a,b = crawl_cate(ul[0]), crawl_cate(ul[1])
    browser.close()
    return a,b
