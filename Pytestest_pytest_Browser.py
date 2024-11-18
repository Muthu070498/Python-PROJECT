import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


#  tear down
@pytest.fixture()

def setup():
    # set the chromeOptions

    option = webdriver.ChromeOptions()
    option.add_experimental_option(name='detach', value=True)
    driver = webdriver.Chrome(option)
    yield driver
    # tear down the webdriver


# def  test_title(setup):
#
#     setup.maximize_window()
#     setup.get('https://www.facebook.com')
#     # to validation assertions
#
#
#     createPage=setup.find_element(By.XPATH,"//a[@href='/pages/create/?ref_type=registration_form']")
#     text=createPage.text
#     result=createPage.is_enabled()
#     assert 'Create a Page' in text
#     assert  True is result
#     createPage.click()

#  parameters is used to pass the multiple set of datas

# @pytest.mark.parametrize("url,username,password",[("muthu","98789"),
#                                                 ("kumar","K^&78")])
# def test_login(setup,username,password):
#     setup.maximize_window()
#     setup.get('https://www.facebook.com')
#     setup.find_element(By.ID,"email").send_keys(username);
#     setup.find_element(By.ID, "pass").send_keys(password);

@pytest.mark.smoke
def testsmoke1():
    print('smoke 1 data')


@pytest.mark.regression
def testregression1():
    print('regression 1 test')

@pytest.mark.smoke
def testsmoke2():
    print('smoke 2 data')


@pytest.mark.sanity
def testregression2():
    print('regression 2 test')



