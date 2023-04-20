import random
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from proxyscrape import create_collector

options = webdriver.ChromeOptions()
options.headless = True

proxies = create_collector('http') # Get a list of HTTP proxies

while True:
    # Select a random proxy
    proxy = random.choice(proxies)
    print('Using proxy:', proxy)

    p = Proxy()
    p.proxy_type = ProxyType.MANUAL
    p.http_proxy = proxy.host + ':' + proxy.port
    p.ssl_proxy = proxy.host + ':' + proxy.port

    capabilities = webdriver.DesiredCapabilities.CHROME
    p.add_to_capabilities(capabilities)

    driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)
    driver.get('https://example.com')
    # Perform desired actions with driver instance
    driver.quit()

    # Wait a random amount of time before selecting a new proxy
    time.sleep(random.randint(10, 60))