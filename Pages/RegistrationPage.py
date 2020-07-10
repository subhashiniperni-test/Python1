from Library import configReader

class RegistrationClass:

    def __init__(self,obj):
        global driver
        driver=obj

    def enter_username(self, username):
        driver.find_element_by_name(configReader.fetchElementLocators("Registration", "username")).send_keys(
            username)

    def enter_email(self,email):
        driver.find_element_by_name(configReader.fetchElementLocators("Registration", "email")).send_keys(
            email)

    def enter_password(self,password):
        driver.find_element_by_name(configReader.fetchElementLocators("Registration", "password")).send_keys(password)
