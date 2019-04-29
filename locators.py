# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """A class for main page locators"""

    CHOOSE_LOCAL = (By.XPATH, '//a[@data-toggle="dropdown"]')
    CHOOSE_KATOWICE = (By.CSS_SELECTOR,'ul.dropdown-menu li:nth-child(4)')

class KatowicePageLocators(object):
    """A class for Katowice page locators."""

    RESERVATION_BTN = (By.XPATH,'//ul[@class="nav"]["Rezerwacja"]')

class RegisterPageLocators(object):
    """A class for search results register locators."""
    NAME_FIELD = (By.NAME, 'name')
    LASTNAME_FIELD = (By.NAME, 'surname')
    EMAIL_FIELD = (By.NAME, 'email')
    PHONE_FIELD = (By.NAME, 'phone')
    PEOPLENB_FIELD = (By.NAME, 'people_number')
    HOUR_FIELD = (By.NAME, 'beginHour')
    MINUTES_FIELD = (By.NAME, 'beginMinute')
    ENDHOUR_FIELD = (By.NAME, 'endHour')
    ENDMINUTES_FIELD = (By.NAME, 'endMinute')
    DATE_FIELD = (By.NAME, 'date')
    DATE_CHOSEN_FIELD = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[1]/a')
    RESERVE_FIELD = (By.XPATH, '//input[@value="Rezerwuj"]')


class ConfPageLocators(object):
    """A class for search results confirmation locators."""
    CONFIRMATION_BUTTON = (By.XPATH, '//a[@class="ok-button"]')
