__author__ = """Cary Hawkins email-hawkinscary23@gmail.com"""
from Base.base import BasePage, InvalidPageException

class HomePage(BasePage):

	def __init__(self, driver):
		super(Homepage, self).__init__(driver)

	def _validate_page(self, driver):
		try:
			driver.find_element_by_link_text("LOGIN")
		except:
			raise InvalidPageException("Page Not Loaded")

