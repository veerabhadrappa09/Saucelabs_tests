import pytest

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils
from time import sleep

class Test_02_Admin_Login_data_driven:
    admin_page_url = Read_config.get_admin_page_url()
    logger = Log_Maker().log_gen()
    path = ".\\test_data\\admin_login_data.xlsx"
    status_list = []

    @pytest.mark.regression
    def test_valid_admin_login_data_driven(self,setup):
        self.logger.info("**************Test valid_admin_login page data driven started***************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.rows = excel_utils.get_row_count(self.path,"Sheet1")
        print("rows: ",self.rows)

        for r in range(2,self.rows+1):
            self.username = excel_utils.read_data(self.path,"Sheet1",r,1).strip()
            self.password = excel_utils.read_data(self.path,"Sheet1",r,2).strip()
            self.exp_login_status = excel_utils.read_data(self.path,"Sheet1",r,3).strip()
            # print(f"username: {self.username}\n, password: {self.password}\n, exp_login_status: {self.exp_login_status}")
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            act_title = self.driver.title
            exp_title = "Swag Labs"
            if act_title == exp_title:
                if self.exp_login_status == "Yes":
                    self.logger.info("Expected login status: Yes")
                    self.logger.info("Test data is passed")
                    self.status_list.append("Pass")
                    self.driver.implicitly_wait(10)
                    self.admin_lp.click_logout()
                    self.logger.info("Logout Button is clicked")

                elif self.exp_login_status == "No":
                    self.logger.info("Expected login status: No")
                    self.logger.info("Test data failed")
                    self.status_list.append("Pass")
            elif act_title != exp_title:
                if self.exp_login_status == "Yes":
                    self.logger.info("Test data is failed")
                    self.status_list.append("Fail")
                elif self.exp_login_status == "No":
                    self.logger.info("Test data passed")
                    self.status_list.append("Pass")
        print("Status list: ",self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test admin data drive test is failed")
            self.driver.quit()
            assert False
        else:
            self.logger.info("Test admin data drive test is passed")
            self.driver.quit()
            assert True
