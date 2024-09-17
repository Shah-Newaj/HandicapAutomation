import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.CFManagerPage import CFManager
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_Add_Recruitment_Request:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger

    def test_CHRM_Approval(self,setup):
        self.logger.info("************* CHRM_Approval **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting CHRM_Approval Test **********")
        self.cfm = CFManager(self.driver)
        self.cfm.clickRecruitmentRequest()
        self.cfm.clickCFM()
        self.cfm.clickEdit()

        self.logger.info("************* Providing CHRM Approval **********")
        #Scroll Down
        flag = self.driver.find_element(By.LINK_TEXT, "Handicap International")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.cfm.setComments("CFM Comment.")
        self.cfm.clickCFMAgree()
        time.sleep(5)
        self.cfm.clickSubmit()
        time.sleep(5)


