import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import data
import locators
import method
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from data import phone_number, message_for_driver
from method import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        service = Service()
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.get(data.urban_routes_url)

        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.routes_page.set_from(data.address_from)
        self.routes_page.set_to(data.address_to)

    def test_pick_comfort(self):
        self.routes_page.request_taxi()
        self.routes_page.pick_comfort()

    def test_set_phone_number(self):
        self.routes_page.set_phone_number()

    def test_set_payment(self):
        self.routes_page.set_payment()

    def test_set_requirements(self):
        self.routes_page.set_requirements()

    def test_call_taxi(self):
        self.routes_page.call_taxi()

    def test_wait_driver_details(self):
        self.routes_page.wait_driver_details()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
