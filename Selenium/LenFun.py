from selenium import webdriver
from  selenium.webdriver.common.by import By
import time

# set the chromeOptions

option=webdriver.ChromeOptions()
option.add_experimental_option(name='detach',value=True)
driver=webdriver.Chrome(option)
driver.maximize_window()
driver.get('https://www.amazon.in/')

# Dynamic Wait
# No such Element Exception -->
driver.implicitly_wait(50)

input=driver.find_element(By.ID,"twotabsearchtextbox")
input.send_keys('Mobile')
search=driver.find_element(By.ID,"nav-search-submit-button")
search.click()


# Static Wait
# 1 sec --> time sleep 9 sec wait
listOfElements=driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")

print(len(listOfElements))

expected = 'Samsung Galaxy'
for i in listOfElements:
    va=i.text

    print(i.tag_name)
    print(va)
    if va.__contains__(expected):
        i.click()
    else:
        print('issue')





