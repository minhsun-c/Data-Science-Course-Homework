from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driverPath = "./chromedriver-mac-arm64/chromedriver"

# Create a Service object
s = Service(executable_path=driverPath)

# Initialize the Service with ChromeDriverManager
s = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=s)
url = 'https://www.cwa.gov.tw/V8/E/W/County/index.html'

browser.get(url)

mapping = {}

blocks = browser.find_elements(By.CSS_SELECTOR, ".icon_zone")
for block in blocks:
    city = block.find_element(By.CLASS_NAME, "city").text
    temp = block.find_element(By.CLASS_NAME, "tem-C").text.split("~")
    mapping[city] = temp[0] + " - " + temp[1]

browser.quit()

input_city = input()
if input_city == 'all':
    for k, v in mapping.items():
        print(k)
        print(v)
else:
    print(input_city)
    print(mapping[input_city])