# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import datetime

class HomePageLocators(object):
    CHOOSE_LOCAL = (By.XPATH, '//a[@data-toggle="dropdown"]')
    CHOOSE_KATOWICE = (By.CSS_SELECTOR,'ul.dropdown-menu li:nth-child(4)')

class KatowicePageLocators(object):
    RESERVATION_BTN = (By.XPATH,'//ul[@class="nav"]["Rezerwacja"]')

class RegisterPageLocators(object):
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
    #Pick current day of the month
    today = datetime.datetime.today().day
    DATE_CHOSEN_FIELD = (By.XPATH, '//a[@class="ui-state-default ui-state-highlight ui-state-hover"]["+today+"]')
    RESERVE_FIELD = (By.XPATH, '//input[@value="Rezerwuj"]')


class ConfPageLocators(object):
    CONFIRMATION_BUTTON = (By.XPATH, '//a[@class="ok-button"]')
