import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_ddt_admin_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("*************** Test_ddt_admin_Login *******************")
        self.logger.info("*************** Verifying Login DDT Test  *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in excel", self.rows)

        lst_status = [] #Empty variable

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)



            act_title = self.driver.title
            exp_title = "Admin - HI HR System"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************** Title is matched and Expected Output is Pass so Test Case Passed *******************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*************** Title is matched but Expected Output is Fail so Test Case Failed *******************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*************** Title is not matched but Expected Output is Pass so Test Case Failed *******************")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*************** Title is not matched and Expected Output is Fail so Test Case Passed *******************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
           self.logger.info("Login DDT Test is Passed...")
           self.driver.close()
           assert True
        else:
           self.logger.info("Login DDT Test is Failed...")
           self.driver.close()
           assert False

        self.logger.info("********** End of Login DDT Test ************")
        self.logger.info("********* Completed Test_ddt_admin_Login *********")
