from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, requests

driverPath = "./chromedriver-mac-arm64/chromedriver"

# Create a Service object
s = Service(executable_path=driverPath)

# Initialize the Service with ChromeDriverManager
s = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=s)
url = 'https://www.cwa.gov.tw/V8/E/W/OBS_Sat.html'

browser.get(url)

RGB = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#Tab1 a')))
RGB.click()

Taiwan = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.inline-group > label:nth-child(3)')))
Taiwan.click()

dropmenu = browser.find_element(By.ID, 'selectday')
date = dropmenu.text.split()[0] + " 09:00"
dropmenu.send_keys(date)

img = browser.find_element(By.CSS_SELECTOR, "#link-1 > img")
imgUrl = img.get_attribute('src')
imgData = requests.get(imgUrl).content

with open('out.jpg', 'wb') as img:
    img.write(imgData)

browser.quit()