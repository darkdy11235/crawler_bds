from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import random
import config


def main():
    while True:
            # chrome options for setting the proxy
            chrome_options = webdriver.ChromeOptions()
            # add argument with proxy infos
            proxy = random.choice(config.ip)
            chrome_options.add_argument(f'--proxy-server={proxy}')
            driver = webdriver.Chrome(options=chrome_options)

            driver.get('https://myexternalip.com/raw')
            print(proxy)
            sleep(2)
            driver.quit()
main()