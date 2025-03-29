
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Dropdownpage:

    def __init__(self,driver):
        self.driver = driver

    fruit_dropdown_button_xpath = "//*[@id='fruits']"
    superman_dropdown_xpath = "//*[@id='superheros']"
    programming_language_xpath = "//*[@id='lang']"
    country_dropdown_xpath = "//*[@id='country']"

    def dropdown(self,element):
        return Select(element)


    def launch_dropdownpage(self):
        self.driver.get("https://letcode.in/dropdowns")

    def select_fruit_dropdown(self):
        fruits = self.driver.find_element(By.XPATH,self.fruit_dropdown_button_xpath)
        opt = self.dropdown(fruits)
        opt.select_by_visible_text("Orange")

    def select_supman_dropdwon(self):
        superheros = self.driver.find_element(By.XPATH,self.superman_dropdown_xpath)
        opt = self.dropdown(superheros)
        opt.select_by_value("cm")

    def select_last_programming_language(self):
        programming_languages = self.driver.find_element(By.XPATH,self.programming_language_xpath)
        select = self.dropdown(programming_languages)
        all_options = select.options
        print(all_options)
        select.select_by_index(len(all_options)-1)  ##5-1  = 4 (index value)

    def select_country_dropdown(self):
        countrys = self.driver.find_element(By.XPATH,self.country_dropdown_xpath)
        allopt = self.dropdown(countrys)
        allopt.select_by_value("India")


