__author__ = """Cary Hawkins email-hawkinscary23@gmail.com"""
from Base.base import BasePage
from selenium.webdriver.support.select import Select
import unittest


class Login(BasePage):
	login_box = "LoginName"
	password_box = "Password"

	def login(self, username, password):
		"""

		:param username: login username for website
		:param password: login password for website
		:return:
		"""
		self.driver.find_element_by_link_text("LOGIN").click()
		self.driver.find_element_by_id(self.login_box).send_keys(username)
		self.driver.find_element_by_id(self.password_box).send_keys(password)
		self.driver.find_element_by_id("loginbutton").click()


	def signup_customer(self, firstname, lastname, email, username, password):
		"""

		:param firstname: First Name of user signing up for website
		:param lastname: Last Name of user signing up for Website
		:param email: email address to validate for user
		:param username: select a username for the user
		:param password: create a password for the user
		:return:
		"""

		self.driver.find_element_by_class_name("signup").click()
		self.driver.find_element_by_id("FirstName").send_keys(firstname)
		self.driver.find_element_by_id("LastName").send_keys(lastname)
		self.driver.find_element_by_id("Email").send_keys(email)
		self.driver.find_element_by_id("ConfirmEmail").send_keys(email)
		self.driver.find_element_by_id("UserName").send_keys(username)
		self.driver.find_element_by_id("Password").send_keys(password)
		self.driver.find_element_by_id("ConfirmPassword").send_keys(password)
		self.driver.find_element_by_xpath(
			'//*[@id="account-registration-form"]/div/div/div/form/div[14]/div[2]/button').click()
		signedup = self.driver.find_element_by_xpath('//*[@id="navigation"]/nav[1]/div/div[2]/ul/li[7]/a').text
		return signedup


class FindDesigner(Login, Select):
	def by_website(self, webaddress):
		"""

        :param webaddress: the first part of the url for the designer ie 'http://johnsmith.origamiowl.com would be everything between the forward slash and the .origamiowl.com
        :return:
        """
		self.driver.find_element_by_xpath('//*[@id="navigation"]/nav[1]/div/div[2]/ul/li[5]/a').click()
		self.driver.find_element_by_id("WebAlias").send_keys(webaddress)
		self.driver.find_element_by_id("webalias-search").click()

	def by_designer_id(self, designerid):
		"""

        :param designerid: the designer id number of the designer being searched for
        :return:
        """
		self.driver.find_element_by_xpath('//*[@id="navigation"]/nav[1]/div/div[2]/ul/li[5]/a').click()
		self.driver.find_element_by_id("DesignerID").send_keys(designerid)
		self.driver.find_element_by_id("distributorId-search").click()

		def by_name(self, firstname, lastname, state):

			"""

			:param firstname: First Name of the Designer being searched for
			:param lastname: Last Name of the Designer Being searched for
			:param state: State where the designer lives
			:return:
			"""
		self.driver.find_element_by_xpath('//*[@id="navigation"]/nav[1]/div/div[2]/ul/li[5]/a').click()
		self.driver.find_element_by_id("dfirst").send_keys(firstname)

		self.driver.find_element_by_id("dlast").send_keys(lastname)
		self.driver.find_element_by_id("dstate").click()
		findstate = Select(self.driver.find_element_by_id("dstate"))
		findstate.select_by_visible_text(state)
		self.driver.find_element_by_id("info-search").click()
		if self.driver.find_element_by_id("noResults"):
			raise Exception("Designer Not Found")
		else:
			self.driver.find_element_by_link_text("CHOOSE").click()


class Shopping(Login):
	def collections(self, collection):
		"""

		:param collection: Name of the collection ie. inscriptions
		:return:
		"""
		self.driver.find_element_by_link_text("COLLECTIONS").click()
		self.driver.find_element_by_link_text(collection.upper()).click()

	def categories(self, category):
		"""

		:param category: Name of the Category ie Living Lockets
		:return:
		"""
		self.driver.find_element_by_link_text("CATEGORIES").click()
		self.driver.find_element_by_link_text(category.upper()).click()

	def shop(self):
		self.driver.find_element_by_link_text("SHOP").click()

	def cart(self):
		self.driver.find_element_by_class_name("shopping-items-count").click()

	def checkout(self):
		self.driver.find_element_by_xpath('//*[@id="view-cart"]/div/div[2]/div/div/div[2]/a').click()

	def guest_checkout(self, firstname, lastname, email, country, address1, address2, city, state, zip):
		"""

		:param firstname: First Name of Guest
		:param lastname: Last Name of Guest
		:param email: valid email address of *@*.*
		:param country: United States or Canada
		:param address1: Street Address
		:param address2: Apartment etc.
		:param city: Valid City name
		:param state: Choose from list of states and Territories, including Puerto Rico, Guam, American Samoa,
		Northern Mariana Islands, United States Minor Outlying Islands, AA/AE/AP Military, Virgin Islands,
		And District of Columbia abbreviated as D.C.
		:param zip: Vaild 5 digit Zip Code or 6 alpha numeric zip code for Canada
		:return:
		"""
		self.driver.find_element_by_xpath('//*[@id="view-sitelogin"]/div[2]/div[3]/a').click()
		self.driver.find_element_by_id("Address_FirstName").send_keys(firstname)
		self.driver.find_element_by_id("Address_LastName").send_keys(lastname)
		self.driver.find_element_by_id("Address_Email").send_keys(email)
		country1 = Select(self.driver.find_element_by_id("Address_Country"))
		country1.select_by_visible_text(country)
		self.driver.find_element_by_id("Address_Address1").send_keys(address1)
		self.driver.find_element_by_name("Address.Address2").send_keys(address2)
		self.driver.find_element_by_id("Address_City").send_keys(city)
		self.driver.find_element_by_name("Address.State").click()
		state1 = Select(self.driver.find_element_by_name("Address.State"))
		state1.select_by_visible_text(state)
		self.driver.find_element_by_id("Address_Zip").send_keys(zip)
		self.driver.find_element_by_xpath('//*[@id="view-ordershipping"]/div[2]/div/form/div[3]/button').click()

	def guest_cc_(self, name, cardnumber, expmonth, expyear):
		"""

		:param name: Full name on cc
		:param cardnumber: credit card number without dashes
		:param expmonth: month number of expiration month
		:param expyear: year number of expiration year
		:return: None
		"""
		self.driver.find_element_by_xpath('//*[@id="view-orderpayment"]/div/div[1]/p/a').click()
		self.driver.find_element_by_name("NewCard.NameOnCard").send_keys(name)
		self.driver.find_element_by_name("NewCard.CardNumber").send_keys(cardnumber)
		self.driver.find_element_by_name("NewCard.ExpirationMonth").click()
		month = Select(self.driver.find_element_by_name("NewCard.ExpirationMonth"))
		month.select_by_value(expmonth)
		self.driver.find_element_by_name("NewCard.ExpirationYear").click()
		year = Select(self.driver.find_element_by_name("NewCard.ExpirationYear"))
		year.select_by_value(expyear)
		self.driver.find_element_by_xpath('//*[@id="form0"]/button').click()

	def place_order(self, shipping, changebilladdress, changeshipaddress, jbcode):
		"""

		:param shipping: Standard, 2 day, Overnight
		:param changebilladdress: Y or N only
		:param changeshipaddress: Y or N only
		:param jbcode: Leave blank if this is not a jewelry bar order
		:return: None
		"""
		shipmethods = (
			"Standard",
			"2 Day",
			"Overnight"
		)
		self.driver.find_elements_by_name("ShipMethodID")[shipmethods.index(shipping)].click()
		if changebilladdress == "Y":
			self.driver.find_element_by_xpath(
				'//*[@id="view-shoppingreview"]/div[2]/div[1]/div[1]/div/div/div[2]/a/i').click()
		elif changeshipaddress == "Y":
			self.driver.find_element_by_xpath(
				'//*[@id="view-shoppingreview"]/div[2]/div[1]/div[1]/div/div/div[1]/a').click()
		elif jbcode is not "":
			self.driver.find_element_by_id("partyId").send_keys(jbcode)
			self.driver.find_element_by_id("btnUserPartyId").click()
		else:
			self.driver.find_element_by_id("btnPlaceOrder").click()


class HostJB(Login, unittest.TestCase):
	def host_new_jb(self):
		self.driver.find_element_by_link_text("HOST A JEWELRY BAR").click()
		self.driver.is_element_present(id, "hostess")