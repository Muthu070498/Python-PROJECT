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
driver.implicitly_wait(10)

input=driver.find_element(By.ID,"twotabsearchtextbox")
print(input)
input.send_keys('Mobile')
search=driver.find_element(By.ID,"nav-search-submit-button")
search.click()



listOfElements=driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
print(listOfElements)
print(len(listOfElements))
expected='POCO C61 Ethereal Blue 4GB RAM 64GB ROM'
for i in listOfElements:
    print(i.text)
    actual=i.text
    if actual.__eq__(expected):
        i.click()


allId=driver.window_handles
for i in allId:
    driver.switch_to.window(i)
    actualTitle=driver.title
    print(actualTitle)



addToCart=driver.find_element(By.ID,"add-to-cart-button")

driver.execute_script("window.scrollBy(0, 500);")
addToCart.click()
print('Done')

