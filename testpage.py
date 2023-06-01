from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestLocators:
    LOCATOR_LOGIN = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, """#app > main > nav > ul > li:nth-child(2) > a""")
    LOCATOR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_BUTTON = (By.CSS_SELECTOR, """#contact > div.submit > button > span""")
    


class Operations(BasePage):
    def enter_login(self, word):
        logging.info(f"Send '{word}' to element {TestLocators.LOCATOR_LOGIN[1]}")
        input1 = self.find_element(TestLocators.LOCATOR_LOGIN)
        input1.clear()
        input1.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send '{word}' to element {TestLocators.LOCATOR_PASS[1]}")
        input2 = self.find_element(TestLocators.LOCATOR_PASS)
        input2.clear()
        input2.send_keys(word)

    def click_login_button(self):
        self.find_element(TestLocators.LOCATOR_LOGIN_BTN).click()
    
    def click_contact_button(self):
        self.find_element(TestLocators.LOCATOR_CONTACT_BTN).click()

    def enter_name(self, word):
        logging.info(f"Send '{word}' to element {TestLocators.LOCATOR_NAME[1]}")
        name_field = self.find_element(TestLocators.LOCATOR_NAME)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email(self, word):
        logging.info(f"Send '{word}' to element {TestLocators.LOCATOR_EMAIL[1]}")
        email_field = self.find_element(TestLocators.LOCATOR_EMAIL)
        email_field.clear()
        email_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send '{word}' to element {TestLocators.LOCATOR_CONTENT[1]}")
        content_field = self.find_element(TestLocators.LOCATOR_CONTENT)
        content_field.clear()
        content_field.send_keys(word)

    def click_contact_button3(self):
        logging.info('Click button "Contact us"')
        self.find_element(TestLocators.LOCATOR_CONTACT_BUTTON).click()

    def alllert(self):
        logging.info("Alert")
        text = self.alert()
        logging.info(text)
        return text