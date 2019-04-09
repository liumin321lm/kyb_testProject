from appium import webdriver
import yaml
import logging
import logging.config
from selenium.common.exceptions import NoSuchAttributeException

# logging.basicConfig(level=logging.INFO,filename='./log/runlog.log',
#                     format='%(asctime)s %(filename)s [line:%(lineno)d]%(levelname)s %(message)s')



CON_LOG='../log/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    file = open('../desired_caps.yaml', 'r')
    data = yaml.safe_load(file)
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['platformVersion']=data['platformVersion']

    desired_caps['app']=data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']
    logging.info('start app...')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(10)
    return driver
if __name__ == '__main__':
    appium_desired()


