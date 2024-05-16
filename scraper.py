from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

f = open("link.txt")
line = f.readline()

while line:
    print(line)
    #driver.implicitly_wait(10)
    driver.get(line)
    sleep(5)
    print(driver.title)
    line = f.readline()

f.close()

# driver.get('https://www.tmp.link/?tmpui_page=/app&listview=login')
# driver.get_screenshot_as_file('foo.png')

