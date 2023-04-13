import time
from pages.element_page import *

class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextboxPage(driver, "https;//demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            time.sleep(5)
            print(full_name, email, current_address, permanent_address)