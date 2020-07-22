from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')

driver.get('https://www.naver.com')

time.sleep(10)

driver.close()