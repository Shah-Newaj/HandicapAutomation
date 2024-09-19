import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.CFManagerPage import CFManager
from pageObjects.CHRManagerPage import CHRManager
from pageObjects.HODPage import HOD
from pageObjects.HiringManagerPage import HiringManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_Recruitment_Request_DDT:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    path = ".//TestData/RecruitmentRequest.xlsx"
    logger = LogGen.loggen()

    def test_recruitment_request_ddt(self,setup):
        self.logger.info("*************** Test_ddt_admin_Login *******************")
        self.logger.info("*************** Verifying Login DDT Test  *******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* Login succesful **********")

        self.logger.info("************* Starting Recruitment Request DDT **********")

        self.rows = XLUtils.getRowCount(self.path, 'addRequest')
        print("Number of rows in excel", self.rows)

        lst_status = [] #Empty variable

        for r in range(2, self.rows+1):
            self.project = XLUtils.readData(self.path,'addRequest', r, 1)
            self.hmanager = XLUtils.readData(self.path, 'addRequest', r, 2)
            self.vposition = XLUtils.readData(self.path, 'addRequest', r, 3)
            self.jobdes = XLUtils.readData(self.path, 'addRequest', r, 4)
            self.npos = XLUtils.readData(self.path, 'addRequest', r, 5)
            self.pemployee = XLUtils.readData(self.path, 'addRequest', r, 6)
            self.location = XLUtils.readData(self.path, 'addRequest', r, 7)
            self.appointment = XLUtils.readData(self.path, 'addRequest', r, 8)
            self.jobstartdate = XLUtils.readData(self.path, 'addRequest', r, 9)
            self.jobenddate = XLUtils.readData(self.path, 'addRequest', r, 10)
            self.vacancycaused = XLUtils.readData(self.path, 'addRequest', r, 11)
            self.salaryrangefrom = XLUtils.readData(self.path, 'addRequest', r, 12)
            self.recruitmenttype = XLUtils.readData(self.path, 'addRequest', r, 13)
            self.hod = XLUtils.readData(self.path, 'addRequest', r, 14)
            self.salaryrangeto = XLUtils.readData(self.path, 'addRequest', r, 15)
            self.comments = XLUtils.readData(self.path, 'addRequest', r, 16)


            self.addreq = HiringManager(self.driver)
            self.addreq.clickRecruitmentRequest()
            self.addreq.clickHiringManager()
            self.addreq.clickAddNew()

            self.logger.info("************* Providing recruitment request info **********")
            self.addreq.selectProject(self.project)
            self.addreq.setHiringManager(self.hmanager)
            self.addreq.setVacantPosition(self.vposition)
            self.addreq.selectJobDescription(self.jobdes)
            self.addreq.setNumberofPosition(self.npos)
            self.addreq.selectPresentEmployee(self.pemployee)
            self.addreq.setLocation(self.location)
            self.addreq.selectAppointment(self.appointment)
            self.addreq.setJobStartDate(self.jobstartdate)
            self.addreq.setJobEndingDate(self.jobenddate)
            self.addreq.setVacancyCaused(self.vacancycaused)
            self.addreq.setSalaryRangeFrom(self.salaryrangefrom)
            self.addreq.selectRecruitmentType(self.recruitmenttype)
            time.sleep(2)
            self.addreq.selectHOD(self.hod)
            self.addreq.setSalaryRangeTo(self.salaryrangeto)
            self.addreq.setComments(self.comments)
            time.sleep(3)
            flag = self.driver.find_element(By.LINK_TEXT, "Handicap International")
            self.driver.execute_script("arguments[0].scrollIntoView();", flag)
            time.sleep(2)
            self.addreq.clickSubmit()

        self.logger.info("************* Starting Edit Recruitment Request DDT **********")

        self.rows = XLUtils.getRowCount(self.path, 'editRequest')
        print("Number of rows in excel", self.rows)

        lst_status = []  # Empty variable

        for r in range(2, self.rows + 1):
            self.project = XLUtils.readData(self.path, 'editRequest', r, 1)
            self.hmanager = XLUtils.readData(self.path, 'editRequest', r, 2)
            self.vposition = XLUtils.readData(self.path, 'editRequest', r, 3)
            self.jobdes = XLUtils.readData(self.path, 'editRequest', r, 4)
            self.npos = XLUtils.readData(self.path, 'editRequest', r, 5)
            self.pemployee = XLUtils.readData(self.path, 'editRequest', r, 6)
            self.location = XLUtils.readData(self.path, 'editRequest', r, 7)
            self.appointment = XLUtils.readData(self.path, 'editRequest', r, 8)
            self.jobstartdate = XLUtils.readData(self.path, 'editRequest', r, 9)
            self.jobenddate = XLUtils.readData(self.path, 'editRequest', r, 10)
            self.vacancycaused = XLUtils.readData(self.path, 'editRequest', r, 11)
            self.salaryrangefrom = XLUtils.readData(self.path, 'editRequest', r, 12)
            self.recruitmenttype = XLUtils.readData(self.path, 'editRequest', r, 13)
            self.hod = XLUtils.readData(self.path, 'editRequest', r, 14)
            self.salaryrangeto = XLUtils.readData(self.path, 'editRequest', r, 15)
            self.comments = XLUtils.readData(self.path, 'editRequest', r, 16)

            self.editreq = HiringManager(self.driver)
            # self.editreq.clickRecruitmentRequest()
            # self.editreq.clickHiringManager()
            self.editreq.clickEdit()

            self.logger.info("************* Providing edit recruitment request info **********")
            self.editreq.selectProject(self.project)
            self.editreq.setHiringManager(self.hmanager)
            self.editreq.setVacantPosition(self.vposition)
            self.editreq.selectJobDescription(self.jobdes)
            self.editreq.setNumberofPosition(self.npos)
            self.editreq.selectPresentEmployee(self.pemployee)
            self.editreq.setLocation(self.location)
            self.editreq.selectAppointment(self.appointment)
            self.editreq.setJobStartDate(self.jobstartdate)
            self.editreq.setJobEndingDate(self.jobenddate)
            self.editreq.setVacancyCaused(self.vacancycaused)
            self.editreq.setSalaryRangeFrom(self.salaryrangefrom)
            self.editreq.selectRecruitmentType(self.recruitmenttype)
            time.sleep(2)
            self.editreq.selectHOD(self.hod)
            self.editreq.setSalaryRangeTo(self.salaryrangeto)
            self.editreq.setComments(self.comments)
            time.sleep(3)
            flag = self.driver.find_element(By.LINK_TEXT, "Handicap International")
            self.driver.execute_script("arguments[0].scrollIntoView();", flag)
            time.sleep(2)
            self.editreq.clickSubmit()

        self.logger.info("******* Starting HOD_Approval Test **********")
        self.hod = HOD(self.driver)
        # self.hod.clickRecruitmentRequest()
        self.hod.clickHOD()
        self.hod.clickEdit()

        self.logger.info("************* Providing HOD Approval **********")
        self.hod.selectCHRManager("1")
        self.hod.selectCFManager("9")
        # Scroll Down
        flag = self.driver.find_element(By.LINK_TEXT, "Handicap International")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.hod.setComments("HOD Comment.")
        self.hod.clickHODAgree()
        self.hod.clickSubmit()
        time.sleep(5)

        self.logger.info("******* Starting CHRM_Approval Test **********")
        self.chrm = CHRManager(self.driver)
        # self.chrm.clickRecruitmentRequest()
        self.chrm.clickCHRM()
        self.chrm.clickEdit()

        self.logger.info("************* Providing CHRM Approval **********")
        # Scroll Down
        flag = self.driver.find_element(By.LINK_TEXT, "Handicap International")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.chrm.setComments("CHRM Comment.")
        self.chrm.clickCHRMAgree()
        time.sleep(5)
        self.chrm.clickSubmit()
        time.sleep(5)

        self.logger.info("******* Starting CFM_Approval Test **********")
        self.cfm = CFManager(self.driver)
        # self.cfm.clickRecruitmentRequest()
        self.cfm.clickCFM()
        self.cfm.clickEdit()

        self.logger.info("************* Providing CFM Approval **********")
        # Scroll Down
        flag = self.driver.find_element(By.LINK_TEXT, "Handicap International")
        self.driver.execute_script("arguments[0].scrollIntoView();", flag)
        self.cfm.setComments("CFM Comment.")
        self.cfm.clickCFMAgree()
        time.sleep(5)
        self.cfm.clickSubmit()
        time.sleep(5)

        self.logger.info("********** End of Recruitment Request DDT Test ************")
        self.logger.info("********* Completed Test_Recruitment_Request_DDT *********")
