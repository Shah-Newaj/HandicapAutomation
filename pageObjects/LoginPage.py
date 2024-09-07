from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    txt_loginUserName = "username"
    txt_loginPassword = "password"
    btn_login = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.NAME, self.txt_loginUserName).clear()
        self.driver.find_element(By.NAME, self.txt_loginUserName).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME, self.txt_loginPassword).clear()
        self.driver.find_element(By.NAME, self.txt_loginPassword).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login).click()