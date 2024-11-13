# BrowserLaunch

from selenium import webdriver
import time

# set the chromeOptions

option=webdriver.ChromeOptions()
option.add_experimental_option(name='detach',value=True)
driver=webdriver.Chrome(option)
driver.maximize_window()
driver.get('https://www.facebook.com')


# navigations
driver.get('https://www.youtube.com')

driver.back()

time.sleep(5)

path=r'C:\Users\kutty\PycharmProjects\SP002New\Selenium\Screenshot\img1.png'
driver.save_screenshot(path)
driver.forward()
driver.refresh()

pageUrl=driver.current_url
print(pageUrl)
pageTitle=driver.title
print(pageTitle)

# screenshot

