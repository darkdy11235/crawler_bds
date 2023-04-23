import random
import time
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from app.crawler.data.path import *
from app.crawler.models.some_model import loai, batdongsan
from app.crawler.data.url import domain, site_map


class create_driver():
    def __init__(self, option):
        options = FirefoxOptions()
        if option == 0:
            options.add_argument("--headless")
        self.__driver = webdriver.Firefox(options=options)

    def get_driver(self):
        return self.__driver


def crawl_proxy():
    with create_driver(0).get_driver() as browser:
        browser.get("https://www.freeproxylists.net")
        list_proxy = []
        for tr in browser.find_elements(By.TAG_NAME,"tbody")[1].find_elements(By.TAG_NAME,"tr")[1:]:
            try:
                list_proxy.append(tr.find_element(By.TAG_NAME, "a").text + ":" + tr.find_elements(By.TAG_NAME,"td")[1].text)
                print(list_proxy[-1])
            except:
                pass
    return list_proxy


def crawl_cate(ul):
    result = []
    list_a = ul.find_elements(By.TAG_NAME,"a")
    for i in range(1,len(list_a)):
        r = loai(list_a[i].text, list_a[i].get_attribute("href"))
        result.append(r)
    return result

def crawl_loai_thue_loai_ban():
    browser = create_driver(0).get_driver()
    browser.get(domain + site_map)
    ul = browser.find_elements(By.CLASS_NAME,"sitemapblock_row1")
    r1 = crawl_cate(ul[0])
    r2 = crawl_cate(ul[1])
    browser.close()
    return r1,r2

def crawl_all_link(loai,range_page):
    all_links_of_loai = []
    next_page_url = loai.link
    for loop in range(0, range_page):
        driver = create_driver(0).get_driver()
        driver.get(next_page_url)
        print("loop number-" + str(loop + 1))
        time.sleep(3)

        SCROLL_PAUSE_TIME = 0.2
        new_height = 0

        while True:
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = new_height + 1000
            if new_height == 9000:
                break

        lists = driver.find_elements(By.CLASS_NAME, "js__product-link-for-product-id")
        for j in lists:
            all_links_of_loai.append(j.get_attribute("href"))
        try:
            buttons = driver.find_elements(By.CLASS_NAME, "re__pagination-icon")
            next_page_url = buttons[-1].get_attribute("href")
        except:
            driver.close()
            pass
        driver.close()
    return all_links_of_loai

def find(driver,xpath):
    try:
        return driver.find_element(By.XPATH,xpath)
    except:
        return None

def find_all(driver,xpath):
    try:
        return driver.find_elements(By.XPATH,xpath)
    except:
        return None

def crawl_post(url):
    post = batdongsan()
    driver = create_driver(0).get_driver()
    driver.get(url)

    try:
        sdt = find_all(driver,phone_number_path)[0].text.split(" ")
        post.sdt = sdt[0] + sdt[1] + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    except:
        print("not found phone number")
        pass

    try:
        x = find(driver,title_path).text
        post.tieude = x
        try:
            post.tieude = x[0:x.index(sdt[0:3])] + sdt
        except:
            pass

    except:
        print("not found tieude")
        pass

    try:
        post.mota = find(driver,description_path).text
    except:
        print("not found mota")
        pass

    try:
        post.diachi = find(driver,address_path).text
    except:
        post.diachi = "not found"
        print("not found diachi")
        pass

    try:
        gia = find(driver,price_path).text.split(" ")
        if gia[1] == ("triệu"):
            gia = float(gia[0]) * 1000000
        elif gia[1] == ("tỷ"):
            gia = float(gia[0]) * 1000000000
        else:
            gia = float(gia[0])
        post.gia = gia
    except:
        print("not found gia")
        pass

    try:
        dientich = find(driver,area_path).text
        post.dientich = float(dientich.split(" ")[0])
    except:
        print("not found dientich")
        pass

    try:
        post.sophongngu = int(find(driver,bedroom_path).text.split(" ")[0])
    except:
        print("not found phongngu")
        pass

    try:
        post.nguoidang = find(driver,user_name_path).text
    except:
        print("not found nguoidang")
        pass

    try:
        time.sleep(2)
        anh = find_all(driver,image_path)
        for i in range(0,len(anh)):
            if i == 0:
                anh[i] = anh[i].get_attribute("src")
            else:
                anh[i] = anh[i].get_attribute("data-src")
        post.anh ='[' + ",".join(anh) + ']'
    except:
        post.anh = "[https://photo2.tinhte.vn/data/attachment-files/2021/03/5385458_cover_heheboi.jpg]"
        print("not found anh")
        pass
    driver.close()
    return post
