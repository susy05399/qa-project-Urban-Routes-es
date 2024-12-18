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
        time.sleep(2)
        cls.routes_page = method.UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_from(address_from)
        self.routes_page.set_to(address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_pick_comfort(self):
        self.routes_page.request_taxi()
        self.routes_page.pick_comfort()
        comfort_status = self.routes_page.get_comfort_status()
        assert comfort_status == True

    def test_set_phone_number(self):
        self.routes_page.set_phone_number()
        phone_number = data.phone_number
        assert self.routes_page.get_phone_number() == phone_number

    def test_set_payment(self):
        self.routes_page.set_payment()
        assert self.routes_page.get_payment() == 'Tarjeta'

    def test_set_message(self):
        self.routes_page.set_message()
        message_for_driver = data.message_for_driver
        assert self.routes_page.get_message() == message_for_driver

    def test_set_requirements(self):
        self.routes_page.set_requirements()
        assert self.routes_page.get_helado_counter() == '2'
        assert self.routes_page.get_slider_status() == True

    def test_call_taxi(self):
        self.routes_page.call_taxi()
        order_header_title = self.routes_page.get_order_header_title()
        assert  'Buscar automóvil' in order_header_title

    def test_wait_driver_details(self):
        time.sleep(30)
        order_header_title = self.routes_page.get_order_header_title()
        assert 'El conductor llegará' in order_header_title

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()