from selenium.webdriver.common.by import By
import time

class Alertpage:

    def __init__(self,driver):
        self.driver = driver


    alert_url = "https://the-internet.herokuapp.com/javascript_alerts"
    js_alert_xpath ="//*[@id='content']/div/ul/li[1]/button"
    js_confirm_xpath = "//*[@id='content']/div/ul/li[2]/button"
    js_prompt_xpath = "//*[@id='content']/div/ul/li[3]/button"


    def launch_alert_url(self):
        self.driver.get(self.alert_url)

    def click_js_alert_accept(self):
        self.driver.find_element(By.XPATH,self.js_alert_xpath).click()
        self.driver.switch_to.alert.accept()
        time.sleep(4)

    def click_confirm_alert_accept(self):
        self.driver.find_element(By.XPATH,self.js_confirm_xpath).click()
        self.driver.switch_to.alert.accept()
        time.sleep(4)

    def click_confirm_alert_dismiss(self):
        self.driver.find_element(By.XPATH,self.js_confirm_xpath).click()
        self.driver.switch_to.alert.dismiss()
        time.sleep(4)

    def click_prompt_alert_accept(self):
        self.driver.find_element(By.XPATH,self.js_prompt_xpath).click()
        alert = self.driver.switch_to.alert
        alert.send_keys("Hello my name is rahul ")
        alert.accept()
    def click_prompt_alert_dismiss(self):
        self.driver.find_element(By.XPATH,self.js_prompt_xpath).click()
        alert =self.driver.switch_to.alert
        alert.send_keys("Hello my name is rahul ")
        alert.dismiss()