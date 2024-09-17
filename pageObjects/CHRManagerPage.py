from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CHRManager:
    link_RecruitmentRequest_menu_xpath = "//a[normalize-space()='Recruitment Request']"
    link_c_hr_manager_menu_link = "C HR Manager"
    action_btn_edit_xpath = "(//i[@class='fa fa-edit'])[1]"
    txt_comment_id = "chrm_comment"
    chk_CHRM_Agree_name = "chrm_status"
    btn_confirm_submit_name = "save_and_update"
    link_footer_link = "Handicap International"

    def __init__(self, driver):
        self.driver = driver

    def clickRecruitmentRequest(self):
        self.driver.find_element(By.XPATH, self.link_RecruitmentRequest_menu_xpath).click()


    def clickCHRM(self):
        self.driver.find_element(By.LINK_TEXT, self.link_c_hr_manager_menu_link).click()

    def clickEdit(self):
        self.driver.find_element(By.XPATH, self.action_btn_edit_xpath).click()

    def setComments(self, comments):
        self.driver.find_element(By.ID, self.txt_comment_id).clear()
        self.driver.find_element(By.ID, self.txt_comment_id).send_keys(comments)

    def clickCHRMAgree(self):
        self.driver.find_element(By.NAME, self.chk_CHRM_Agree_name).click()

    def clickSubmit(self):
        self.driver.find_element(By.NAME, self.btn_confirm_submit_name).click()