from locators import KatowicePageLocators
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class KatowicePage(BasePage):

    def click_reserv_button(self):
        element = self.driver.find_element(*KatowicePageLocators.RESERVATION_BTN)
        element.click()
