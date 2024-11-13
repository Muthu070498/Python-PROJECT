from selenium import webdriver
from  selenium.webdriver.common.by import By
import time
# set the chromeOptions

option=webdriver.ChromeOptions()
option.add_experimental_option(name='detach',value=True)
driver=webdriver.Chrome(option)
driver.maximize_window()


def alert():
    driver.get('https://letcode.in/alert')
    # simpleAlert=driver.find_element(By.ID,"accept")
    # print(simpleAlert.is_enabled())
    # simpleAlert.click()
    # time.sleep(5)
    # driver.switch_to.alert.accept()
    #
    #
    #
    # confirmAlert = driver.find_element(By.ID,"confirm")
    # print(confirmAlert.is_enabled())
    # confirmAlert.click()
    # time.sleep(5)
    # driver.switch_to.alert.dismiss()
    #
    #
    # promptAlert=driver.find_element(By.ID,"prompt")
    # print(promptAlert.is_enabled())
    # promptAlert.click()
    # time.sleep(5)
    # driver.switch_to.alert.send_keys("Greens")
    # time.sleep(5)
    # driver.switch_to.alert.accept()

    modernAlert = driver.find_element(By.ID, "modern")
    modernAlert.click()
    button = driver.find_element(By.XPATH, "//button[@aria-label='close']")
    button.click()

def frame():
    driver.get('https://letcode.in/frame')
    driver.switch_to.frame(0)
    firstName=driver.find_element(By.NAME,"fname")
    firstName.send_keys("Muthu")

    # innerFrame=driver.find_element(By.XPATH,"//iframe[@src='innerFrame']")
    driver.switch_to.frame(1)
    email=driver.find_element(By.NAME,"email")
    email.send_keys("king@gmail.com")

    driver.switch_to.frame(0)
    lastName = driver.find_element(By.NAME, "lname")
    lastName.send_keys("Kumar")


frame()
