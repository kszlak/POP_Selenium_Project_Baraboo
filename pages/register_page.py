from locators import RegisterPageLocators
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RegisterPage(BasePage):

    def add_name_field(self, valid_name):
        field = self.driver.find_element(*RegisterPageLocators.NAME_FIELD)
        field.send_keys(valid_name)

    def add_lastname_field(self, valid_lastname):
        field = self.driver.find_element(*RegisterPageLocators.LASTNAME_FIELD)
        field.send_keys(valid_lastname)

    def add_email_field(self, valid_email):
        field = self.driver.find_element(*RegisterPageLocators.EMAIL_FIELD)
        field.send_keys(valid_email)

    def add_phone_field(self, valid_phone):
        field = self.driver.find_element(*RegisterPageLocators.PHONE_FIELD)
        field.send_keys(valid_phone)

    def add_peoplenb_field(self, valid_peoplenb):
        field = self.driver.find_element(*RegisterPageLocators.PEOPLENB_FIELD)
        field.send_keys(valid_peoplenb)

    def add_hour_field(self, valid_hour):
        field = self.driver.find_element(*RegisterPageLocators.HOUR_FIELD)
        field.send_keys(valid_hour)

    def add_minutes_field(self, valid_minutes):
        field = self.driver.find_element(*RegisterPageLocators.MINUTES_FIELD)
        field.send_keys(valid_minutes)

    def add_endhour_field(self, valid_endhour):
        field = self.driver.find_element(*RegisterPageLocators.ENDHOUR_FIELD)
        field.send_keys(valid_endhour)

    def add_endminutes_field(self, valid_endminutes):
        field = self.driver.find_element(*RegisterPageLocators.ENDMINUTES_FIELD)
        field.send_keys(valid_endminutes)

    def click_date_field(self):
        element = self.driver.find_element(*RegisterPageLocators.DATE_FIELD)
        element.click()

    def click_datechosen_field(self):
        element = self.driver.find_element(*RegisterPageLocators.DATE_CHOSEN_FIELD)
        element.click()

    def click_reserve_field(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RegisterPageLocators.RESERVE_FIELD))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RegisterPageLocators.RESERVE_FIELD))
        element = self.driver.find_element(*RegisterPageLocators.RESERVE_FIELD)
        element.click()
