import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.HiringManagerPage import HiringManager
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Add_Recruitment_Request:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger


    def test_addRecruitmentRequest(self,setup):
        self.logger.info("************* Add_Recruitment_Request **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add_Recruitment_Request Test **********")
        # self.driver = setup
        self.addreq = HiringManager(self.driver)
        self.addreq.clickRecruitmentRequest()
        self.addreq.clickHiringManager()
        self.addreq.clickAddNew()

        self.logger.info("************* Providing recruitment request info **********")
        self.addreq.selectProject("MEAL")
        self.addreq.setHiringManager("Abdullah")
        self.addreq.setVacantPosition("Sqa Automation Pytest")
        self.addreq.selectJobDescription("Supply Chain Officer")
        self.addreq.setNumberofPosition("5")
        self.addreq.selectPresentEmployee("Yes")
        self.addreq.setLocation("Dhaka")
        self.addreq.selectAppointment("Permanent")
        self.addreq.setJobStartDate("20-08-2024")
        self.addreq.setJobEndingDate("31-12-2025")
        self.addreq.setVacancyCaused("Resignation")
        self.addreq.setSalaryRangeFrom("60000")
        self.addreq.selectRecruitmentType("External Recruitment")
        self.addreq.selectHOD("1")
        self.addreq.setSalaryRangeTo("80000")
        self.addreq.setComments("As the potential candidate are available externally, we have decided to try to find the candidate through external recruitment process first.")
        time.sleep(3)
        flag = self.driver.find_element(By.NAME, "save_and_update")
        self.driver.execute_script("arguments[0].scrollIntoView();",flag)
        time.sleep(2)
        # self.addreq.clickSubmit()
