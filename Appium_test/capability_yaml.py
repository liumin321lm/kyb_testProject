from appium import webdriver
import yaml
import logging
import logging.config
from selenium.common.exceptions import NoSuchAttributeException

# logging.basicConfig(level=logging.INFO,filename='./log/runlog.log',
#                     format='%(asctime)s %(filename)s [line:%(lineno)d]%(levelname)s %(message)s')

file=open('desired_caps.yaml','r')
data=yaml.safe_load(file)

CON_LOG='./log/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

desired_caps={}
desired_caps['platformName']=data['platformName']
desired_caps['deviceName']=data['deviceName']
desired_caps['platformVersion']=data['platformVersion']

desired_caps['app']=data['app']
desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']
desired_caps['noReset']=data['noReset']
# desired_caps['unicodeKeyboard']=True
# desired_caps['resetKeyboard']=True
logging.info('start app...')
driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
driver.implicitly_wait(10)


def check_cancelBtn():
    logging.info('check cancelBtn')
    try:
        cancelBtn=driver.find_element_by_id('android:id/button2')
    except NoSuchAttributeException:
        logging.info('no cancel')
    else:
        cancelBtn.click()

def check_skipBtn():
    logging.info('check skipBtn')
    try:
        skipBtn=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchAttributeException:
        logging.info('no skipBtn')
    else:
        skipBtn.click()

check_cancelBtn()

check_skipBtn()