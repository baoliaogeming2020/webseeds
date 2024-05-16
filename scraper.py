from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

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

f = open("link.txt")               # 返回一个文件对象 
line = f.readline()               # 调用文件的 readline()方法 
while line: 
    #print line,                   # 后面跟 ',' 将忽略换行符 
    print(line)　      # 在 Python 3 中使用 
    line = f.readline() 
 
f.close()  

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://www.tmp.link/?tmpui_page=/app&listview=login')
# driver.get_screenshot_as_file('foo.png')
print(driver.title)
