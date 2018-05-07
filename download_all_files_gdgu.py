from selenium import *
from selenium import webdriver
import time

DRIVER = 'C:/chromedriver.exe'
driver = webdriver.Chrome(DRIVER)
website = 'https://sites.google.com/site/gdguinternetofthings' #enter the gdgu website here
driver.get(website + '/file-cabinet/') 

continue_link = driver.find_elements_by_link_text('Download')
for i in range(0,len(continue_link)):
	continue_link[i].click()
	time.sleep(5)
