import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.RecruitmentRequest.test_addRecruitmentRequest import Test_Add_Recruitment_Request

@allure.severity(allure.severity_level.CRITICAL)
class Test_admin_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    # @allure.severity(allure.severity_level.MINOR)
    def test_login(self,setup):
        self.logger.info("*************** Test_admin_Login *******************")
        self.logger.info("*************** Verifying Login Test  *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Admin - HI HR System":
            assert True
            self.logger.info("*************** Login Test is Passed *******************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="testLoginScreen",attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.logger.error("*************** Login Test is Failed *******************")
            assert False
