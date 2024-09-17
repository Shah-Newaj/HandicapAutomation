from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HOD:
    link_RecruitmentRequest_menu_xpath = "//a[normalize-space()='Recruitment Request']"
    link_HOD_menu_link = "HOD"
    # btn_AddNew_link = "Add New"
    action_btn_edit_xpath = "(//i[@class='fa fa-edit'])[1]"
    drp_C_HR_Manager_id = "chrm_id"
    drp_C_F_Manager_id = "cfm_id"
    txt_comment_id = "comments"
    chk_HOD_Agree_name = "hodam_status"
    btn_confirm_submit_name = "save_and_update"

    def __init__(self, driver):
        self.driver = driver

    def clickRecruitmentRequest(self):
        self.driver.find_element(By.XPATH, self.link_RecruitmentRequest_menu_xpath).click()


    def clickHOD(self):
        self.driver.find_element(By.LINK_TEXT, self.link_HOD_menu_link).click()

    def clickEdit(self):
        self.driver.find_element(By.XPATH, self.action_btn_edit_xpath).click()

    def selectCHRManager(self,chrm):
        chrmanager_value = self.driver.find_element(By.ID, self.drp_C_HR_Manager_id)
        chrmanager_name = Select(chrmanager_value)
        chrmanager_name.select_by_value(chrm)

    def selectCFManager(self,cfm):
        cfmanager_value = self.driver.find_element(By.ID, self.drp_C_F_Manager_id)
        cfmanager_name = Select(cfmanager_value)
        cfmanager_name.select_by_value(cfm)
    def setComments(self, comments):
        self.driver.find_element(By.ID, self.txt_comment_id).clear()
        self.driver.find_element(By.ID, self.txt_comment_id).send_keys(comments)

    def clickHODAgree(self):
        self.driver.find_element(By.NAME, self.chk_HOD_Agree_name).click()

    def clickSubmit(self):
        self.driver.find_element(By.NAME, self.btn_confirm_submit_name).click()