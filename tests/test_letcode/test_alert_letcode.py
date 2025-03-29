import time

from pages.letcode_alertpage import Alertpage
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class Testalert:

    def test_simple_alert(self):
        alert_page = Alertpage(self.driver)
        alert_page.launch_alert_page()
        alert_page.click_simple_alert_button()

    def test_confirm_alert(self):
        alert_page = Alertpage(self.driver)
        alert_page.launch_alert_page()
        alert_page.click_confirm_alert_button()

    def test_prompt_alert(self):
        alert_page =Alertpage(self.driver)
        alert_page.launch_alert_page()
        alert_page.click_prompt_alert_button()

    def test_modern_alert(self):
        alert_page =Alertpage(self.driver)
        alert_page.launch_alert_page()
        alert_page.click_modern_alert_button()


