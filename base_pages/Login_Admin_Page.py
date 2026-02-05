from selenium.webdriver.common.by import By
from time import sleep


class Login_Admin_Page:
    text_box_username = "user-name"
    text_box_password = "password"
    btn_login = "login-button"
    logout_menu = "react-burger-menu-btn"
    Logout_link_text = "Logout"



    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.ID,self.text_box_username).clear()
        self.driver.find_element(By.ID,self.text_box_username).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.text_box_password).clear()
        self.driver.find_element(By.ID,self.text_box_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID,self.btn_login).click()

    def click_logout(self):
        self.driver.find_element(By.ID,self.logout_menu).click()
        sleep(3)
        self.driver.find_element(By.LINK_TEXT,self.Logout_link_text).click()





