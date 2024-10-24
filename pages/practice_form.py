from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
import allure
from base.base_page import BasePage
from config.urls import Urls
from data.data_generator import TestDataGenerator
import random


class PracticeForm(BasePage):
    PAGE_URL = Urls.PRACTICE_FORM

    FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
    EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
    GENDER_RADIO_BUTTON = {
        "Male": ("xpath", "//label[@for='gender-radio-1']"),
        "Female": ("xpath", "//label[@for='gender-radio-2']"),
        "Other": ("xpath", "//label[@for='gender-radio-3']")
    }
    MOBILE_NUMBER_FIELD = ("xpath", "//input[@id='userNumber']")
    DATE_OF_BIRTH_FIELD = ("xpath", "//input[@id='dateOfBirthInput']")
    SELECT_YEAR_CALENDAR = ("xpath", "//select[@class='react-datepicker__year-select']")
    SELECT_MONTH_CALENDAR = ("xpath", "//select[@class='react-datepicker__month-select']")
    SELECT_DAY_CALENDAR = ("xpath", "//div[@role='option']")
    SUBJECTS_FIELD = ("xpath", "//input[@id='subjectsInput']")
    HOBBIES_FIELD = {
        "Sports": ("xpath", "//label[@for='hobbies-checkbox-1']"),
        "Reading": ("xpath", "//label[@for='hobbies-checkbox-2']"),
        "Music": ("xpath", "//label[@for='hobbies-checkbox-3']")
    }
    CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
    STATE_FIELD = ("xpath", "//div[@id='state']")
    SELECTED_ITEMS = ("xpath", "//div[@tabindex='-1']")
    CITY_FIELD = ("xpath", "//div[@id='city']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")

    TABLE_VALUES = ("xpath", "//div[@class='table-responsive']//td[2]")

    def __init__(self, driver):
        super().__init__(driver)
        self.data_generator = TestDataGenerator()

    @allure.step("Enter first name")
    def enter_first_name(self):
        self.first_name = self.data_generator.generate_first_name()
        self.element_is_clickable(self.FIRST_NAME_FIELD).send_keys(self.first_name)

    @allure.step("Enter last name")
    def enter_last_name(self):
        self.last_name = self.data_generator.generate_last_name()
        self.element_is_clickable(self.LAST_NAME_FIELD).send_keys(self.last_name)

    @allure.step("Enter email")
    def enter_email(self):
        self.email = self.data_generator.generate_email()
        self.element_is_clickable(self.EMAIL_FIELD).send_keys(self.email)

    @allure.step("Click radio button")
    def choose_random_radio_button_gender(self):
        self.random_gender = random.choice(list(self.GENDER_RADIO_BUTTON.keys()))
        locator = self.GENDER_RADIO_BUTTON[self.random_gender]
        self.element_is_clickable(locator).click()

    @allure.step("Enter Mobile")
    def enter_mobile_number(self):
        self.mobile_number = self.data_generator.generate_mobile_number()
        self.element_is_clickable(self.MOBILE_NUMBER_FIELD).send_keys(self.mobile_number)

    @allure.step("Complete calendar Mobile")
    def complete_calendar(self):
        self.element_is_clickable(self.DATE_OF_BIRTH_FIELD).click()

        year_dropdown = self.element_is_presence(self.SELECT_YEAR_CALENDAR)
        select_year = Select(year_dropdown)
        years = select_year.options
        random_year = random.choice(years)
        random_year.click()

        month_dropdown = self.element_is_presence(self.SELECT_MONTH_CALENDAR)
        select_month = Select(month_dropdown)
        months = select_month.options
        random_month = random.choice(months)
        random_month.click()

        days = self.elements_are_presence(self.SELECT_DAY_CALENDAR)
        random_day = self.get_random_element(days)
        random_day.click()

    @allure.step("Select subjects")
    def choose_subjects(self):
        self.element_is_clickable(self.SUBJECTS_FIELD).click()
        self.subjects = self.element_is_presence(self.SUBJECTS_FIELD)
        list(map(lambda _: self.subjects.send_keys(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')), range(3, 7)))
        self.subjects.send_keys(Keys.TAB)

    @allure.step("Click on a random number of hobbies checkboxes")
    def choose_random_checkboxes_hobbies(self):
        self.random_hobbies = random.sample(list(self.HOBBIES_FIELD.values()), random.randint(1, len(self.HOBBIES_FIELD)))
        list(map(lambda locator: (self.scroll_to(locator), self.element_is_clickable(locator).click()),
                 self.random_hobbies))

    @allure.step("Enter current address")
    def enter_current_address(self):
        self.current_address = self.data_generator.generate_current_address()
        self.element_is_clickable(self.CURRENT_ADDRESS_FIELD).send_keys(self.current_address)

    @allure.step("Select state")
    def select_state(self):
        self.element_is_presence(self.STATE_FIELD).click()
        dropdown_items = self.elements_are_presence(self.SELECTED_ITEMS)
        self.random_state = random.choice(dropdown_items)
        self.random_state.click()

    @allure.step("Select city")
    def select_city(self):
        self.element_is_presence(self.CITY_FIELD).click()
        dropdown_items = self.elements_are_presence(self.SELECTED_ITEMS)
        self.random_city = random.choice(dropdown_items)
        self.random_city.click()

    @allure.step("Click submit button")
    def click_submit(self):
        self.scroll_to(self.SUBMIT_BUTTON)
        self.element_is_clickable(self.SUBMIT_BUTTON).click()

    @allure.step("Taking received value")
    def taking_received_values(self):
        result_value_list = self.elements_are_visible(self.TABLE_VALUES)
        data_values = []
        for i in result_value_list:
            self.scroll_to(i)
            data_values.append(i.text)
        return data_values

    @allure.step("Check presents elements")
    def check_present_corrected_data_in_table(self):
        values = self.taking_received_values()
        assert self.first_name + ' ' + self.last_name in values, f"Full name '{self.first_name} {self.last_name}' was not found in values: {values}"
        assert self.email in values, f"Email '{self.email}' was not found in values: {values}"
        assert self.random_gender in values, f"Gender '{self.random_gender}' was not found in values: {values}"
        assert self.mobile_number in values, f"Mobile number '{self.mobile_number}' was not found in values: {values}"
        assert self.current_address in values, f"Address '{self.current_address}' was not found in values: {values}"
        self.random_state = self.element_is_presence(self.STATE_FIELD).text
        self.random_city = self.element_is_presence(self.CITY_FIELD).text
        assert self.random_state + ' ' + self.random_city in values, f"Combination '{self.random_state} {self.random_city}' was not found in values: {values}"