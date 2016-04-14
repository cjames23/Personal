__author__ = """Cary Hawkins email-hawkinscary23@gmail.com"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class BaseTestCase(unittest.TestCase):

	def setUp(self, platform, browser, url):
		desired_caps = {}
		desired_caps['platform'] = self.platform
		desired_caps['browserName']= self.browser
		self.base_url = self.url
		self.verificationErrors = []
		self.accept_next_alert = True
		driver = self.driver
		driver.maximize_window()
		driver.get(self.base_url + "/")
		driver.implicitly_wait(15)

	def is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how,value=what)
		except NoSuchElementException:
			return False
		return True

	def is_alert_present(self):
		try:
			self.driver.switch_to.alert.text()
		except NoAlertPresentException:
			return False
		return True

	def close_alert_and_get_text(self):
		try:
			alert = self.driver.switch_to.alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally:
			self.accept_next_alert = True

	def click_wait(self, button, timeout=10):
		source = self.driver.page_source
		button.click()

		def compare_source(driver):
			try:
				return source != driver.page_source
			except NoSuchElementException:
				print("Failed")
		WebDriverWait(self.driver, timeout).until(compare_source)

	def tearDown(self):
		self.driver.quit()

