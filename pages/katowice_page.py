from locators import KatowicePageLocators
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class KatowicePage(BasePage):

    def click_reserv_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(KatowicePageLocators.RESERVATION_BTN))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(KatowicePageLocators.RESERVATION_BTN))
        element = self.driver.find_element(*KatowicePageLocators.RESERVATION_BTN)
        element.click()
