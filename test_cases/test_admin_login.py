import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker

class Test_01_Admin_Login:
    admin_page_url = Read_config.get_admin_page_url()
    username = Read_config.get_username()
    password = Read_config.get_password()
    invalid_username = Read_config.get_invalid_username()
    logger = Log_Maker().log_gen()

    @pytest.mark.regression
    def test_title_verifications(self,setup):
        self.logger.info("**************Test_01_Admin_Login********************")
        self.logger.info("**************verification of admin login page title********************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        actual_title = self.driver.title
        expected_title = "Swag Labs"
        if actual_title == expected_title:
            self.logger.info("**************Test title_verifications is matched*****************")
            assert True
            self.driver.quit()
        else:
            self.logger.info("**************Test title_verifications is NOT matched***************")
            self.driver.save_screenshot(".\\screenshots\\test_title_verifications.png")
            self.driver.quit()
            assert False


    @pytest.mark.regression
    @pytest.mark.sanity
    def test_valid_admin_login(self,setup):
        self.logger.info("**************Test valid_admin_login page***************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_logo = self.driver.find_element(By.XPATH,"//div[@class='app_logo']").text
        if act_logo == "Swag Labs":
            self.logger.info("**************Test valid_admin_login is valid***************")
            assert True
            self.driver.quit()
        else:
            self.logger.info("**************Test valid_admin_login is NOT valid***************")
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.quit()
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
        self.logger.info("**************Test invalid_admin_login page***************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_msg = self.driver.find_element(By.XPATH,"//h3[@data-test='error']").text
        if error_msg == "Epic sadface: Username and password do not match any user in this service":
            self.logger.info("**************Test invalid_admin_login is Expected error***************")
            assert True
            self.driver.quit()
        else:
            self.logger.info("**************Test invalid_admin_login is NOT Expected error***************")
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.quit()
            assert False


