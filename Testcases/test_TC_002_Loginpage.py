from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from Library import configReader
from BaseFiles import InitiateBrowser
import time
import pytest
from Pages import LoginPage

def test_multiwindow():
    driver = InitiateBrowser.startBrowser()
    driver.find_element_by_xpath(configReader.fetchElementLocators1('LoginPage','Login')).click()
    login=LoginPage.LoginPage1(driver)
    login.enter_Lusername("test")
    login.enter_Lpassword("test")
    driver.find_element_by_xpath(configReader.fetchElementLocators1('LoginPage','Submit')).click()
    """
    driver.find_element_by_xpath(configReader.fetchElementLocators1('LoginPage','Click_Myaccount')).click()
    driver.find_element_by_xpath(configReader.fetchElementLocators1('LoginPage','Click_Update')).click()
    
    allwin = driver.window_handles
    Mainwin = ""
    for win in allwin:
        driver.switch_to.window(win)
        # print(driver.current_url)
        if (driver.current_url == "https://www.thetestingworld.com/testings/manage_customer.php"):
            driver.find_element_by_xpath("//button[text()='Start Download']").click()
            time.sleep(5)
            driver.close()
        elif (driver.current_url == "https://www.thetestingworld.com/testings/dashboard.php"):
            Mainwin = win

    driver.switch_to.window(Mainwin)
    print(driver.current_url)
    """