from common.myunit import StartEnd
from businessView.loginView import LoginView
import unittest
import logging

from common.desired_caps import appium_desired

class TestLogin(StartEnd):
    csv_file = '../data/account.csv'

    def test_login_1(self):
        logging.info('=====test_login_1=====')

        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())


if __name__ == '__main__':
    unittest.main()
