from selenium.webdriver.support.select import Select

from pages.letcode_dropdownpage import Dropdownpage
import time
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class Test_dropdown:

    def test_fruit_dropdown(self):
        dp = Dropdownpage(self.driver)
        dp.launch_dropdownpage()
        dp.select_fruit_dropdown()
        time.sleep(4)

    def test_superman_dropdown(self):
        dp = Dropdownpage(self.driver)
        dp.launch_dropdownpage()
        dp.select_supman_dropdwon()
        time.sleep(4)

    def test_programming_language_dropdown(self):
        dp = Dropdownpage(self.driver)
        dp.launch_dropdownpage()
        dp.select_last_programming_language()
        time.sleep(2)

    def test_country_dropdown(self):
        country = Dropdownpage(self.driver)
        country.launch_dropdownpage()
        country.select_country_dropdown()
        time.sleep(3)