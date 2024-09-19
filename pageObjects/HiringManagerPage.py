from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class HiringManager:
    link_RecruitmentRequest_menu_xpath = "//a[normalize-space()='Recruitment Request']"
    link_HiringManager_menu_xpath = "//a[normalize-space()='Hiring Manager']"
    btn_AddNew_link = "Add New"
    # add_new = "xpath://a[normalize-space()='Add New']" this will also work for "Add New" button
    # RecruitmentRequest - RecruitmentRequest Form Page Elements
    drp_project_id = "department"
    txt_name_of_HM_id = "name_of_department"
    txt_position_title_id = "position_title"
    drp_job_des_name = "job_description"
    txt_number_pos_id = "number_of_position"
    drp_present_employee_name = "employee_at_present"
    txt_location_id = "location"
    drp_appointment_type_id = "appointment_type"
    txt_job_starting_date_id = "job_starting_date"
    txt_job_ending_date_id = "job_ending_date"
    txt_vacancy_caused_id = "vacancy_caused_due_to"
    txt_salary_range_from_id = "salary_range_from"
    drp_recruitment_type_name = "recruitment_type"
    drp_hod_id = "hodam_id"
    txt_salary_range_to_id = "salary_range_to"
    txt_comment_id = "comments"
    btn_save_draft_name = "save"
    btn_confirm_submit_name = "save_and_update"
    action_btn_edit_xpath = "(//i[@class='fa fa-edit'])[1]"  # Must Change RecruitmentRequest ID in every run

    def __init__(self, driver):
        self.driver = driver

    def clickRecruitmentRequest(self):
        self.driver.find_element(By.XPATH, self.link_RecruitmentRequest_menu_xpath).click()


    def clickHiringManager(self):
        self.driver.find_element(By.XPATH, self.link_HiringManager_menu_xpath).click()

    def clickAddNew(self):
        self.driver.find_element(By.LINK_TEXT, self.btn_AddNew_link).click()

    def clickEdit(self):
        self.driver.find_element(By.XPATH, self.action_btn_edit_xpath).click()

    def selectProject(self, project):
        project_value = self.driver.find_element(By.ID, self.drp_project_id)
        project_name = Select(project_value)
        project_name.select_by_visible_text(project)
    def setHiringManager(self, hmanager):
        self.driver.find_element(By.ID, self.txt_name_of_HM_id).clear()
        self.driver.find_element(By.ID, self.txt_name_of_HM_id).send_keys(hmanager)

    def setVacantPosition(self, vposition):
        self.driver.find_element(By.ID, self.txt_position_title_id).clear()
        self.driver.find_element(By.ID, self.txt_position_title_id).send_keys(vposition)

    def selectJobDescription(self, jobdes):
        jobdescription_value = self.driver.find_element(By.ID, self.drp_job_des_name)
        jobdescritoin_name = Select(jobdescription_value)
        jobdescritoin_name.select_by_visible_text(jobdes)

    def setNumberofPosition(self, npos):
        self.driver.find_element(By.ID, self.txt_number_pos_id).clear()
        self.driver.find_element(By.ID, self.txt_number_pos_id).send_keys(npos)

    def selectPresentEmployee(self, pemployee):
        presentemployee_value = self.driver.find_element(By.ID, self.drp_present_employee_name)
        presentemployee_name = Select(presentemployee_value)
        presentemployee_name.select_by_visible_text(pemployee)

    def setLocation(self, location):
        self.driver.find_element(By.ID, self.txt_location_id).clear()
        self.driver.find_element(By.ID, self.txt_location_id).send_keys(location)

    def selectAppointment(self, appoinment):
        appoinment_value = self.driver.find_element(By.ID, self.drp_appointment_type_id)
        appoinment_name = Select(appoinment_value)
        appoinment_name.select_by_visible_text(appoinment)

    def setJobStartDate(self, jobstartdate):
        self.driver.find_element(By.ID, self.txt_job_starting_date_id).clear()
        self.driver.find_element(By.ID, self.txt_job_starting_date_id).send_keys(jobstartdate)

    def setJobEndingDate(self, jobenddate):
        self.driver.find_element(By.ID, self.txt_job_ending_date_id).clear()
        self.driver.find_element(By.ID, self.txt_job_ending_date_id).send_keys(jobenddate)

    def setVacancyCaused(self, vacancycaused):
        self.driver.find_element(By.ID, self.txt_vacancy_caused_id).clear()
        self.driver.find_element(By.ID, self.txt_vacancy_caused_id).send_keys(vacancycaused)

    def setSalaryRangeFrom(self, salaryrangefrom):
        self.driver.find_element(By.ID, self.txt_salary_range_from_id).clear()
        self.driver.find_element(By.ID, self.txt_salary_range_from_id).send_keys(salaryrangefrom)

    def selectRecruitmentType(self, recruitmenttype):
        recruitmenttype_value = self.driver.find_element(By.ID, self.drp_recruitment_type_name)
        recruitmenttype_name = Select(recruitmenttype_value)
        recruitmenttype_name.select_by_visible_text(recruitmenttype)

    def selectHOD(self, hod):
        hod_value = self.driver.find_element(By.ID, self.drp_hod_id)
        hod_name = Select(hod_value)
        hod_name.select_by_visible_text(hod)

    def setSalaryRangeTo(self, salaryrangeto):
        self.driver.find_element(By.ID, self.txt_salary_range_to_id).clear()
        self.driver.find_element(By.ID, self.txt_salary_range_to_id).send_keys(salaryrangeto)

    def setComments(self, comments):
        self.driver.find_element(By.ID, self.txt_comment_id).clear()
        self.driver.find_element(By.ID, self.txt_comment_id).send_keys(comments)

    def clickSubmit(self):
        self.driver.find_element(By.NAME, self.btn_confirm_submit_name).click()