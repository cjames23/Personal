__author__ = """Cary Hawkins email-hawkinscary23@gmail.com"""
import time
from selenium.webdriver.support import expected_conditions
from Pages.homepage import HomePage
from Base.basetest import BaseTestCase
from Pages.nav import Login, FindDesigner, Shopping

class ReturnCustomer(BaseTestCase, HomePage, Login):

	def text_bad_login(self):
		base = BaseTestCase()
		base.setUp("WIN8","chrome","https://www.o2testingsandboxone.lz/")
		HomePage(self.driver)
		login = Login()
		login.login("bob1","blahblah")
		self.assertFalse(expected_conditions.invisibility_of_element_located("Login Failed"))
		time.sleep(5)

	def test_good_login(self):
		HomePage(self.driver)
		login = Login()
		login.login("","")
		self.assertTrue(expected_conditions.invisibility_of_element_located("Login Failed"))
		time.sleep(5)

