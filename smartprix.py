from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

website ='https://www.smartprix.com/mobiles'

driver = webdriver.Chrome(options=options)

driver.get(website)

#select out_of_stock,exclude_upcoming checkbox
out_of_stock=driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/aside/div/div[5]/div[2]/label[1]/input')
out_of_stock.click()

upcoming=driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/aside/div/div[5]/div[2]/label[2]/input')
upcoming.click()

#Getting the height of wesite loaded at first sight
old_height=driver.execute_script('return document.body.scrollHeight')
print(old_height)


while True:
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[1]/div[2]/div[3]').click()
    sleep(3)
    new_height=driver.execute_script('return document.body.scrollHeight')

    if new_height==old_height:
        break
    old_height=new_height



#copying html of whole loaded site
html=driver.page_source

with open('Smartphones.html','w',encoding='utf-8') as f:
    f.write(html)