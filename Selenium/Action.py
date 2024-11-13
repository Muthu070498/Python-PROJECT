from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# set the chromeOptions

option=webdriver.ChromeOptions()
option.add_experimental_option(name='detach',value=True)
driver=webdriver.Chrome(option)
driver.maximize_window()
driver.get('https://letcode.in/dropable')

action = ActionChains(driver)

drag=driver.find_element(By.ID,"draggable")
drop=driver.find_element(By.ID,"droppable")
action.drag_and_drop(drag,drop).perform()






def moveto():
    driver.get('https://www.amazon.in/')
    mobile = driver.find_element(By.XPATH, "(//span[@class='nav-line-2'])[1]")

    action = ActionChains(driver)
    action.move_to_element(mobile).perform()

    driver.find_element(By.XPATH, "(//span[text()='தமிழ்'])[1]").click()




