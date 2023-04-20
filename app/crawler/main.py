import time
from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())
from .crawl_category import crawl_loai_thue_loai_ban

loai_thue, loai_ban = crawl_loai_thue_loai_ban()

print(len(loai_thue), len(loai_ban))

from .crawl_by_cate import crawl_cate

for i in loai_thue:
    links = crawl_cate(i)
    time.sleep(4)
    print(len(links))


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
