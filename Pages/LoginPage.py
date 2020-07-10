from Library import configReader

class LoginPage1:

    def __init__(self,obj):
        global driver
        driver = obj
    def  enter_Lusername(self,Lusername):
        driver.find_element_by_name(configReader.fetchElementLocators1('LoginPage', 'Luser')).send_keys(Lusername)
    def enter_Lpassword(self,Lpassword):
        driver.find_element_by_name(configReader.fetchElementLocators1('LoginPage', 'Lpassword')).send_keys(Lpassword)
