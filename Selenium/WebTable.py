from selenium import webdriver
from  selenium.webdriver.common.by import By
import time

# set the chromeOptions

option=webdriver.ChromeOptions()
option.add_experimental_option(name='detach',value=True)
driver=webdriver.Chrome(option)
driver.maximize_window()
driver.get('https://www.worldometers.info/coronavirus/')
driver.implicitly_wait(5)


print(driver.find_element(By.XPATH,"//table//thead").text)