import time

from selenium import  webdriver
from selenium.webdriver.common.by import By


class Alertpage:
    def __init__(self,driver):
        self.driver = driver

    url_alert  = "https://letcode.in/alert"
    simple_alert_button_xpath  = "//*[@id='accept']"
    confirm_alert_button_xpath = "//*[@id='confirm']"
    prompt_alert_button_xpath = "//*[@id='prompt']"
    modern_alert_button_xapth = "//*[@id='modern']"
    modern_alert_cross_button_xpath = "/html/body/app-root/app-alert/section/div/div/div[1]/div/div/div[5]/button"

    def launch_alert_page(self):
        self.driver.get(self.url_alert)

    def click_simple_alert_button(self):
        self.driver.find_element(By.XPATH,self.simple_alert_button_xpath).click()
        simple_alert = self.driver.switch_to.alert
        simple_alert.accept()

    def click_confirm_alert_button(self):
        self.driver.find_element(By.XPATH,self.confirm_alert_button_xpath).click()
        confirm_alert = self.driver.switch_to.alert
        confirm_alert.accept()

    def click_prompt_alert_button(self):
        self.driver.find_element(By.XPATH,self.prompt_alert_button_xpath).click()
        prompt_alert = self.driver.switch_to.alert
        prompt_alert.send_keys("my name is rahul")
        prompt_alert.accept()

    def click_modern_alert_button(self):
        self.driver.find_element(By.XPATH,self.modern_alert_button_xapth).click()




