from pages.pavan_alertpage import Alertpage
import pytest
import time
@pytest.mark.usefixtures("setup_and_teardown")
class Test_alert:

    def test_js_alert(self):
        alertpage = Alertpage(self.driver)
        alertpage.launch_alert_url()
        alertpage.click_js_alert_accept()

    def test_confirm_alert_accept(self):
        alertpage = Alertpage(self.driver)
        alertpage.launch_alert_url()
        alertpage.click_confirm_alert_accept()
        time.sleep(4)

    def test_confirm_alert_dismiss(self):
        alertpage = Alertpage(self.driver)
        alertpage.launch_alert_url()
        alertpage.click_confirm_alert_dismiss()
        time.sleep(2)
    def test_prompt_alert_accept(self):
        alertpage = Alertpage(self.driver)
        alertpage.launch_alert_url()
        alertpage.click_prompt_alert_accept()
        time.sleep(4)
    def test_prompt_alert_dismiss(self):
        alertpage = Alertpage(self.driver)
        alertpage.launch_alert_url()
        alertpage.click_prompt_alert_dismiss()
        time.sleep(4)