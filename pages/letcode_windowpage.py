from selenium.webdriver.common.by import By
import time

class Windowpage:

    def __init__(self,driver):
        self.driver = driver


    window_page_url = "https://letcode.in/window"
    open_home_page_btn_xpath = "//*[@id='home']"
    multiple_window_btn_xpath = "//*[@id='multi']"

    def launch_windowpage(self):
        self.driver.get(self.window_page_url)

    def click_open_homepage_btn(self):
        self.driver.find_element(By.XPATH,self.open_home_page_btn_xpath).click()

    def click_multiple_homepage_btn(self):
        self.driver.find_element(By.XPATH,self.multiple_window_btn_xpath).click()
