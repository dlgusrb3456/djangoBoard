import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/chromedriver.exe')

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

id_input_tag = driver.find_element(By.ID,'id')
id_input_tag.send_keys('dlgsurb3456')
pw_input_tag = driver.find_element(By.ID,'pw')
pw_input_tag.send_keys('?sr06468sr')

time.sleep(3)
login_btn_tag = driver.find_element(By.CLASS_NAME, 'btn_login')
login_btn_tag.click()



time.sleep(5)
driver.quit()

