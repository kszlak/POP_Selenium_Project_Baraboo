from locators import ConfPageLocators
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ConfPage(BasePage):

    def check_registration(self):
        conf_button = self.driver.find_element(*ConfPageLocators.CONFIRMATION_BUTTON)
        assert conf_button.is_displayed()
