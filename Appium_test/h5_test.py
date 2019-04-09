from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from Appium_test.capability import driver
import time
from time import sleep

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:62001'
desired_caps['platforVersion']='5.1.1'

desired_caps['app']=r'E:\BaiduYunDownload\dr.fone3.2.0.apk'
desired_caps['appPackage']='com.wondershare.drfone'
desired_caps['appActivity']='com.wondershare.drfone.ui.activity.WelcomeActivity'

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
# desired_caps['noReset']=True
# desired_caps['unicodeKeyboard']=True
# desired_caps['resetKeyboard']=True
# aa=driver.contexts
# print(aa)
driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()
sleep(10)
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()
sleep(5)
contexts=driver.contexts
print(contexts)
driver.switch_to.context('WEBVIEW_com.wondershare.drfone')

driver.find_element_by_id('email').send_keys('5646541@qq.com')
driver.find_element_by_class_name('btn_send').click()
