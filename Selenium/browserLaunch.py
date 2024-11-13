from selenium import webdriver


option=webdriver.ChromeOptions()
option.add_experimental_option(name='detach',value=True)
option.add_argument('headless')
driver=webdriver.Chrome(option)



# webdriver methods
# maximize the window
driver.maximize_window()
driver.minimize_window()

# get Method is used to launch the url
driver.get('https://www.amazon.in')

# print page current title
pageTitle=driver.title
print(pageTitle)



pageUrl=driver.current_url
print(pageUrl)

if pageUrl.__eq__('https://www.amazon.in/'):
    print(True)

# close the browser
# driver.close()

