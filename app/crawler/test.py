import time
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from some_model import loai, batdongsan, tinh_tp, quan_huyen, phuong_xa, dia_chi
from url import domain, site_map


def crawl_proxy():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    browser = webdriver.Firefox()
    browser.get("https://www.freeproxylists.net")
    tbody = browser.find_elements(By.TAG_NAME,"tbody")
    tr = tbody[1].find_elements(By.TAG_NAME,"tr")
    list_proxy = []
    for i in range(1,len(tr)):
        try:
            td = tr[i].find_elements(By.TAG_NAME,"td")
            list_proxy.append(tr[i].find_element(By.TAG_NAME, "a").text + ":" + td[1].text)
            print(list_proxy[-1])
        except:
            pass
    browser.close()
    return list_proxy

def crawl_cate(ul):
    result = []
    list_a = ul.find_elements(By.TAG_NAME,"a")
    for i in range(1,len(list_a)):
        r = loai(list_a[i].text, list_a[i].get_attribute("href"))
        result.append(r)
    return result

def crawl_loai_thue_loai_ban():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    # browser = webdriver.Firefox()
    browser = webdriver.Firefox()
    browser.get(domain + site_map)
    ul = browser.find_elements(By.CLASS_NAME,"sitemapblock_row1")
    r1 = crawl_cate(ul[0])
    r2 = crawl_cate(ul[1])
    browser.close()
    return r1,r2


def crawl_all_link(list_loai):
    all_links_of_loai = []
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox()
    # driver = webdriver.Firefox()
    k =0
    for i in list_loai:
        if k == 1:
            break
        k+=1
        links_of_loai = []
        driver.get(i.link)
        current_window = driver.current_window_handle
        range_page = 1
        for loop in range(0, range_page):
                print("loop number-" + str(loop + 1))
                time.sleep(2)

                SCROLL_PAUSE_TIME = 0.2
                new_height = 0

                # Get scroll height
                while True:
                    # Scroll down to bottom
                    driver.execute_script("window.scrollBy(0, 1000);")

                    # print(new_height)
                    # print("-")
                    # print(last_height)

                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)

                    # Calculate new scroll height and compare with last scroll height
                    new_height = new_height + 1000
                    if new_height == 9000:
                        break
                # cuoi trang
                links = []
                lists = driver.find_elements(By.CLASS_NAME, "js__product-link-for-product-id")
                for j in lists:
                    links.append(j.get_attribute("href"))
                    print(links[-1])
                try:
                    buttons = driver.find_elements(By.CLASS_NAME, "re__pagination-icon")
                    url = buttons[-1].get_attribute("href")
                    driver.close()
                    driver = webdriver.Firefox()
                    # driver = webdriver.Firefox()
                    driver.get(url)
                except:
                    break
                links_of_loai.append(links)
        all_links_of_loai.append(links_of_loai)
    driver.close()
    return all_links_of_loai


# def crawl_post():
#     with open('proxy.txt', 'r') as file:
#         contents = file.read()
#
#     links = contents.split('\n')
#     all_links_of_post =
#     opts = FirefoxOptions()
#     opts.add_argument("--headless")
#     driver = webdriver.Firefox()
#     # driver = webdriver.Firefox()
#     k =0
#     for i in list_loai:
#         if k == 1:
#             break
#         k+=1
#         links_of_loai = []
#         driver.get(i.link)
#         current_window = driver.current_window_handle
#         range_page = 1
#         for loop in range(0, range_page):
#                 print("loop number-" + str(loop + 1))
#                 time.sleep(2)
#
#                 SCROLL_PAUSE_TIME = 0.2
#                 new_height = 0
#
#                 # Get scroll height
#                 while True:
#                     # Scroll down to bottom
#                     driver.execute_script("window.scrollBy(0, 1000);")
#
#                     # print(new_height)
#                     # print("-")
#                     # print(last_height)
#
#                     # Wait to load page
#                     time.sleep(SCROLL_PAUSE_TIME)
#
#                     # Calculate new scroll height and compare with last scroll height
#                     new_height = new_height + 1000
#                     if new_height == 9000:
#                         break
#                 # cuoi trang
#                 links = []
#                 lists = driver.find_elements(By.CLASS_NAME, "js__product-link-for-product-id")
#                 for j in lists:
#                     links.append(j.get_attribute("href"))
#                     print(links[-1])
#                 try:
#                     buttons = driver.find_elements(By.CLASS_NAME, "re__pagination-icon")
#                     url = buttons[-1].get_attribute("href")
#                     driver.close()
#                     driver = webdriver.Firefox()
#                     # driver = webdriver.Firefox()
#                     driver.get(url)
#                 except:
#                     break
#                 links_of_loai.append(links)
#         all_links_of_loai.append(links_of_loai)
#     driver.close()
#     return all_links_of_loai

r1,r2 = crawl_loai_thue_loai_ban()
all_links_of_loai = crawl_all_link(r1)
# list_proxy = crawl_proxy()

with open('links.txt', 'w') as file:
    for line in all_links_of_loai[0][0]:
        file.write(line + '\n')