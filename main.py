from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.pakwheels.com/used-cars/search/-/')
# Open Webpage on ChromeDriver

flag = True

while flag:
    try:
        btn = driver.find_element_by_xpath("//a[@rel='next']")
        btn.click()
        time.sleep(5)

    except:
        flag = False