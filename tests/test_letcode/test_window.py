import time

from pages.letcode_windowpage import Windowpage

import pytest
@pytest.mark.usefixtures("setup_and_teardown")
class Testwindow:


    def test_window_close_second_window(self):
        window_page = Windowpage(self.driver)
        window_page.launch_windowpage()
        window_page.click_open_homepage_btn()
        ids = self.driver.window_handles
        self.driver.switch_to.window(ids[1])## second window closed
        self.driver.close()
        time.sleep(5)

    def test_window_close_parentwindow(self):
        window_page = Windowpage(self.driver)
        window_page.launch_windowpage()
        parent_window = self.driver.current_window_handle
        window_page.click_open_homepage_btn()
        self.driver.switch_to.window(parent_window)
        self.driver.close()
        time.sleep(5)



