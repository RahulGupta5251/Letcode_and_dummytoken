from pages.letcode_windowpage import Windowpage
import time
import pytest

from pages.pavan_windows import Windowpage_pavan


@pytest.mark.usefixtures("setup_and_teardown")
class Test_window_pavan:

    def test_window_pavan_orange_hrm(self):
        window_page = Windowpage_pavan(self.driver)
        window_page.launch_windowpage()
        window_page.click_orangehrm_link()
        time.sleep(4)
        ids = self.driver.window_handles
        self.driver.switch_to.new_window("tab")
        print(len(ids))
        print(ids)
        for i in ids:
            self.driver.switch_to.window(i)
            if self.driver.title=="OrangeHRM":
                self.driver.close()

        window_page.click_demo_button()
        time.sleep(5)

    def test_launch_multiple_websites(self):
        windowpage = Windowpage_pavan(self.driver)
        windowpage.launch_amazonurl()
        self.driver.execute_script("window.open('', '_blank');")
        ids = self.driver.window_handles
        self.driver.switch_to.window(ids[1])
        windowpage.launchflipcarturl()
        self.driver.execute_script("window.open('', '_blank');")
        ids = self.driver.window_handles
        self.driver.switch_to.window(ids[2])
        windowpage.launch_windowpage()
        time.sleep(4)

    def test_open_new_tab_using_keyboard(self):### see pavan video day-23>>>> min 24 ...
        windowpage = Windowpage_pavan(self.driver)
        windowpage.launch_nopcommerece()
        windowpage.click_register_btn_to_open_in_new_tab_using_keyboard()
        time.sleep(5)

    def test_launch_urls_in_two_new_tab_and_focus_on_new_tab(self):
        window_page = Windowpage_pavan(self.driver)
        window_page.multiple_uRL_launch_in_new_tab()

