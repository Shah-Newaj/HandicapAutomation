import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.HODPage import HOD
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Add_Recruitment_Request:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger

    def test_HOD_Approval(self,setup):
        self.logger.info("************* HOD_Approval **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting HOD_Approval Test **********")
        self.hod = HOD(self.driver)
        self.hod.clickRecruitmentRequest()
        self.hod.clickHOD()
        self.hod.clickEdit()

        self.logger.info("************* Providing HOD Approval **********")
        self.hod.selectCHRManager("1")
        self.hod.selectCFManager("9")
        #Scroll Down
        flag = self.driver.find_element(By.NAME, "save_and_update")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.hod.setComments("HOD Comment.")
        self.hod.clickHODAgree()
        self.hod.clickSubmit()
        time.sleep(5)


