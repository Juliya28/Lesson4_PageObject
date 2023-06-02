from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestLocators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
        
    for i in locators['xpath'].keys():
        ids[i] = (By.XPATH, locators['xpath'][i])  
         
    for i in locators['css'].keys():
        ids[i] = (By.CSS_SELECTOR, locators['css'][i])   


class Operations(BasePage, TestLocators):
    
    with open('./testdata.yaml') as f:
        data = yaml.safe_load(f)
        
        
    def enter_login(self):
        logging.debug('Enter login')
        input1 = self.find_element(self.ids["LOCATOR_LOGIN"])
        input1.clear()
        if input1:
            input1.send_keys(self.data["username"])
        else:
            logging.error('Поле для ввода логина не найдено')
            
            
    def enter_pass(self):
        logging.debug('Enter password')
        input2 = self.find_element(self.ids["LOCATOR_PASS"])
        input2.clear()
        if input2:
            input2.send_keys(self.data["password"])
        else:
            logging.error('Поле для ввода пароля не найдено')
            

    def click_login_button(self):
        logging.debug('Click login button')
        btn = self.find_element(self.ids['LOCATOR_LOGIN_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Кнопка не найдена')
            
    
    def click_contact_button(self):
        logging.debug('Click contuct button')
        btn2 = self.find_element(self.ids['LOCATOR_CONTACT_BTN'])
        if btn2:
            btn2.click()
        else:
            logging.error('Кнопка "Contact" не найдена')
        

    def enter_name(self):
        logging.debug('Enter name')
        name_field = self.find_element(self.ids["LOCATOR_NAME"])
        name_field.clear()
        if name_field:
             name_field.send_keys(self.data["name"])
        else:
            logging.error('Поле для ввода пароля имени не найдено')
           

    def enter_email(self):
        logging.debug('Enter email')
        email_field = self.find_element(self.ids["LOCATOR_EMAIL"])
        email_field.clear()
        if email_field:
            email_field.send_keys(self.data["email"])
        else:
            logging.error('Поле для ввода email имени не найдено')
    

    def enter_content(self):
        logging.debug('Enter content')
        content_field = self.find_element(self.ids["LOCATOR_CONTENT"])
        content_field.clear()
        if content_field:
            content_field.send_keys(self.data["content"])
        else:
            logging.error('Поле для ввода контента имени не найдено')
        

    def click_contact_button3(self):
        logging.debug('Click button "Contact us')
        btn3 = self.find_element(self.ids["LOCATOR_CONTACT_BUTTON"])
        if btn3:
            btn3.click()
        else:
            logging.error('Кнопка не найдена')
        

    def alllert(self):
        logging.debug("Alert")
        text = self.alert()
        logging.info(text)
        return text