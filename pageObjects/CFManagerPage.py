from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CFManager:
    link_RecruitmentRequest_menu_xpath = "//a[normalize-space()='Recruitment Request']"
    link_c_f_manager_menu_link = "C F Manager"
    action_btn_edit_xpath = "(//i[@class='fa fa-edit'])[1]"
    txt_comment_id = "cfm_comment"
    chk_CFM_Agree_name = "cfm_status"
    btn_confirm_submit_name = "save_and_update"

    def __init__(self, driver):
        self.driver = driver

    def clickRecruitmentRequest(self):
        self.driver.find_element(By.XPATH, self.link_RecruitmentRequest_menu_xpath).click()


    def clickCFM(self):
        self.driver.find_element(By.LINK_TEXT, self.link_c_f_manager_menu_link).click()

    def clickEdit(self):
        self.driver.find_element(By.XPATH, self.action_btn_edit_xpath).click()

    def setComments(self, comments):
        self.driver.find_element(By.ID, self.txt_comment_id).clear()
        self.driver.find_element(By.ID, self.txt_comment_id).send_keys(comments)

    def clickCFMAgree(self):
        self.driver.find_element(By.NAME, self.chk_CFM_Agree_name).click()

    def clickSubmit(self):
        self.driver.find_element(By.NAME, self.btn_confirm_submit_name).click()