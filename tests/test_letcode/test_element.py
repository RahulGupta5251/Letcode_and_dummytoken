from selenium.webdriver.common.by import By

from pages.letcode_Elementpage import Elementpage
import time
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class Test_element:


    def test_element(self):

        element_page = Elementpage(self.driver)
        element_page.launch_elementpage()
        element_page.enter_usename()
        element_page.click_continue_btn()
        time.sleep(5)
        result = element_page.validate_image_is_present_and_dispalyed()
        assert result == True
