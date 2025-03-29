from selenium.webdriver.common.by import By


class Framepage:

    def __init__(self,driver):
        self.driver = driver

    frame_url = "https://letcode.in/frame"
    first_name_textbox_xpath = "/html/body/app-root/app-frame-content/div/div/form/div[1]/div/input"
    last_name_textbox_xpath = "/html/body/app-root/app-frame-content/div/div/form/div[2]/div/input"
    email_address_xpath = "/html/body/app-root/app-innerframe/div/div/div/div/div/input"

    def launch_frame_page(self):
        self.driver.get(self.frame_url)
    def enter_first_name(self):
        self.driver.find_element(By.XPATH,self.first_name_textbox_xpath).send_keys("rahul...")

    def enter_lastname(self):
        self.driver.find_element(By.XPATH,self.last_name_textbox_xpath).send_keys("Gupta....")

    def enter_email_address(self):
        self.driver.find_element(By.XPATH,self.email_address_xpath).send_keys("rahulgupta5251@gmail.com")

