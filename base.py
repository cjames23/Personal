__author__ = """Cary Hawkins email-hawkinscary23@gmail.com"""
from abc import abstractmethod

class BasePage(object):
	""" All Page Objects Inherit from this class
	"""
	def _init__(self, driver):
		self._validate_page(driver)
		self.driver = driver

	@abstractmethod
	def _validate_page(self, driver):
		return


class InvalidPageException(Exception):
	print("This is an invalid Page")