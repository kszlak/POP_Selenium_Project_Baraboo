from locators import HomePageLocators
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    def _verify_page(self):
        assert "Pizza z pieca opalanego drewnem w Poznaniu, Katowicach i Lublinie." in self.driver.title

    def click_choose_local(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(HomePageLocators.CHOOSE_LOCAL))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CHOOSE_LOCAL))
        el = self.driver.find_element(*HomePageLocators.CHOOSE_LOCAL)
        el.click()

    def click_choose_katowice(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(HomePageLocators.CHOOSE_KATOWICE))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CHOOSE_KATOWICE))
        el2 = self.driver.find_element(*HomePageLocators.CHOOSE_KATOWICE)
        el2.click()
