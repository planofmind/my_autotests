from base_page import BasePage
from locators.elements_page_locators import *


class TextboxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        full_name = "Ivan Ivanov"
        email = "qwerty@aweq.fd"
        current_address = "SPb"
        permanent_address = "Tver"
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address