from selenium.webdriver.common.by import By

from pages.letcode_frame import Framepage
import pytest
import time
@pytest.mark.usefixtures("setup_and_teardown")
class Testframe:
    inner_frame_xpath = "/html/body/app-root/app-innerframe"

    def test_frame1(self):


        framepage = Framepage(self.driver)
        framepage.launch_frame_page()
        self.driver.switch_to.frame("firstFr")  ## frame name , frameID, frame ny index....0,1,2
        framepage.enter_first_name()
        framepage.enter_lastname()
        time.sleep(5)

    def test_frame2(self):
        framepage = Framepage(self.driver)
        framepage.launch_frame_page()
        self.driver.switch_to.frame("firstFr")
        self.driver.switch_to.frame(1)
        framepage.enter_email_address()
        time.sleep(5)