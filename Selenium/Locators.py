from selenium import webdriver
from  selenium.webdriver.common.by import By
import time

# set the chromeOptions



option=webdriver.ChromeOptions()
option.add_experimental_option(name='detach',value=True)
driver=webdriver.Chrome(option)
driver.maximize_window()
driver.get('https://www.amazon.in/')

driver.implicitly_wait(5)


electronics=driver.find_element(By.XPATH,"(//a[@class='nav-a  '])[5]")
electronics.click()
