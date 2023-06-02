from testpage import Operations
import logging
import time


def test_step1(browser):
    
    logging.info('Starting')
    testpage = Operations(browser)
    testpage.go_to_site()
    testpage.enter_login()
    testpage.enter_pass()
    testpage.click_login_button()
    testpage.click_contact_button()
    time.sleep(2)
    testpage.enter_name()
    testpage.enter_email()
    testpage.enter_content()
    time.sleep(2)
    testpage.click_contact_button3()
    time.sleep(2)
    assert testpage.alert() == 'Form successfully submitted'