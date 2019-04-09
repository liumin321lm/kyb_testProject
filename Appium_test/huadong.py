from Appium_test.capability import driver
from time import sleep


def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y
l=get_size()
print(l)

def swipeleft():
    l=get_size()
    x1=int(l[0]*0.9)
    y1=int(l[0]*0.5)
    x2=int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)

for i in range(2):
    swipeleft()
    sleep(0.5)
driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()