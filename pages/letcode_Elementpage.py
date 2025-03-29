from selenium.webdriver.common.by import By
import pytest
import time


class Elementpage:
    def __init__(self,driver):
        self.driver = driver

    element_url = "https://letcode.in/elements"
    input_text_xpath = "/html/body/app-root/app-home/section/div/div/div[1]/div/div/form/div/p[1]/input"
    search_button_xpath = "//*[@id='search']"
    git_image_xpath = "//img[@alt = 'Placeholder image']"

    def launch_elementpage(self):
        self.driver.get(self.element_url)

    def enter_usename(self):
        self.driver.find_element(By.XPATH,self.input_text_xpath).send_keys("rahul")

    def click_continue_btn(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()
    def validate_image_is_present_and_dispalyed(self):
        image = self.driver.find_element(By.XPATH,self.git_image_xpath)
        return image.is_displayed()

