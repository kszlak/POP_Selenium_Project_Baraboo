# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.katowice_page import KatowicePage
from pages.register_page import RegisterPage
from pages.conf_page import ConfPage
import time
import test_data.customer_data as td


class BarabooRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()

    def setUp(self):
        driver = self.driver
        driver.get("http://baraboo.pl/")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    #def test_page_veryfication(self):
        #home_page = HomePage(self.driver)
        #home_page._verify_page()

    def test_correct_registration(self):
        home_page = HomePage(self.driver)
        home_page._verify_page()
        home_page = HomePage(self.driver)
        home_page.click_choose_local()
        home_page.click_choose_katowice()
        katowice_page = KatowicePage(self.driver)
        katowice_page.click_reserv_button()
        register_page = RegisterPage(self.driver)
        register_page.add_name_field(td.valid_name)
        register_page.add_lastname_field(td.valid_lastname)
        register_page.add_email_field(td.valid_email)
        register_page.add_phone_field(td.valid_phone)
        register_page.add_peoplenb_field(td.valid_peoplenb)
        register_page.add_hour_field(td.valid_hour)
        register_page.add_minutes_field(td.valid_minutes)
        register_page.add_endhour_field(td.valid_endhour)
        register_page.add_endminutes_field(td.valid_endminutes)
        register_page.click_date_field()
        register_page.click_datechosen_field()
        register_page.click_reserve_field()
        conf_page = ConfPage(self.driver)
        conf_page.check_registration()
        
if __name__ == "__main__":
    unittest.main()
