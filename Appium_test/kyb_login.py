from Appium_test.capability import driver,NoSuchElementException
#from appium import webdriver
#from selenium.common.exceptions import NoSuchElementException
def login():
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('liumin321')

    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('65138954')
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

try:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
except NoSuchElementException:
    login()
else:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
    login()