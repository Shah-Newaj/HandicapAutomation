import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_admin_Login:
    baseURL = "https://test.jobs.hi-bd.org/admin/login"
    username = "admin"
    password = "123456"

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Admin - HI HR System123":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False
