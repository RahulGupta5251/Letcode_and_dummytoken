from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

class Windowpage_pavan:

    def __init__(self,driver):
        self.driver =driver

    window_url = "https://opensource-demo.orangehrmlive.com/"
    demo_button_xpath = "//*[@id='navbarSupportedContent']/div[2]/ul/li[1]/a/button"
    amazon_url = "https://www.amazon.in/"
    flipkart_url = "https://www.flipkart.com/"
    nopcommerce_url = "https://demo.nopcommerce.com/"


    def launch_windowpage(self):
        self.driver.get(self.window_url)


    def click_orangehrm_link(self):
        self.driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
        time.sleep(5)

    def click_demo_button(self):
        self.driver.find_element(By.XPATH,self.demo_button_xpath).click()

    def launch_amazonurl(self):
        self.driver.get(self.amazon_url)

    def launchflipcarturl(self):
        self.driver.get(self.flipkart_url)


    def launch_nopcommerece(self):
        self.driver.get(self.nopcommerce_url)

    def click_register_btn_to_open_in_new_tab_using_keyboard(self):
        regilink = Keys.CONTROL + Keys.RETURN
        self.driver.find_element(By.LINK_TEXT,"Register").send_keys(regilink)
        time.sleep(10)


    def multiple_uRL_launch_in_new_tab(self):
        self.driver.get(self.amazon_url)
        self.driver.switch_to.new_window("tab")
        self.driver.get(self.flipkart_url)
        self.driver.switch_to.new_window("tab")
        self.driver.get(self.nopcommerce_url)
        time.sleep(6)
