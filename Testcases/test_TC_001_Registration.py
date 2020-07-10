from selenium.webdriver import Chrome
from BaseFiles import InitiateBrowser
from Library import configReader
from selenium.webdriver.support.select import Select
from Pages import RegistrationPage
import pytest
from DataGen import UserData

@pytest.mark.parametrize('data',UserData.dataGenerator())
def test_Registration(data):
    driver = InitiateBrowser.startBrowser()
    register=RegistrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
    register.enter_email("email")
"""
    # working on confrim password
    driver.find_element_by_name(configReader.fetchElementLocators("Registration","c_password")).send_keys("123456")

    # working on phone
    driver.find_element_by_name(configReader.fetchElementLocators("Registration","phone_number")).send_keys("1234567890")

    # working on date of birth
    driver.find_element_by_name("dob").send_keys("18/12/1988")

    # work on drop down
    obj = Select(driver.find_element_by_name("sex"))
    obj.select_by_visible_text("Male")
    # time.sleep(20)
    # working on radio button
    driver.find_element_by_xpath("//input[@value='home']").click()

    # working on check box
    driver.find_element_by_name("terms").click()

    # working on Button
    driver.find_element_by_xpath("//input[@type='submit']").click()

    # working on Links
    driver.find_element_by_link_text("Read Detail").click()

    driver.close()

"""
