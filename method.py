from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import data
import time
import locators

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, address_from):
        self.driver.find_element(*locators.UrbanRoutesPage.from_field).send_keys(data.address_from)
        time.sleep(1)

    def set_to(self, to_address):
        self.driver.find_element(*locators.UrbanRoutesPage.to_field).send_keys(data.address_to)
        time.sleep(1)

    def get_from(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.to_field).get_property('value')

    def request_taxi(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(locators.UrbanRoutesPage.taxi_button))
        self.driver.find_element(*locators.UrbanRoutesPage.taxi_button).click()
        time.sleep(1)

    def pick_comfort(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(locators.UrbanRoutesPage.comfort))
        self.driver.find_element(*locators.UrbanRoutesPage.comfort).click()
        time.sleep(1)

    def get_comfort_status(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.comfort).is_enabled()

    def set_phone_number(self):
        self.driver.find_element(*locators.UrbanRoutesPage.phone_field).click()

        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.phone_field_popup))

        self.driver.find_element(*locators.UrbanRoutesPage.phone_field_popup).send_keys(data.phone_number)
        time.sleep(1)

        self.driver.find_element(*locators.UrbanRoutesPage.phone_summit_button).click()
        time.sleep(1)

        self.driver.find_element(*locators.UrbanRoutesPage.code_field).send_keys(retrieve_phone_code(self.driver))
        time.sleep(1)

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(locators.UrbanRoutesPage.code_summit_button))

        self.driver.find_element(*locators.UrbanRoutesPage.code_summit_button).click()
        time.sleep(3)

    def get_phone_number(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.phone_field_text).text

    def set_payment(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(locators.UrbanRoutesPage.payment_method_field))

        self.driver.find_element(*locators.UrbanRoutesPage.payment_method_field).click()
        time.sleep(1)

        self.driver.find_element(*locators.UrbanRoutesPage.add_card).click()
        time.sleep(1)

        self.driver.find_element(*locators.UrbanRoutesPage.card_number_field).send_keys(data.card_number)

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(locators.UrbanRoutesPage.card_number_field))

        self.driver.find_element(*locators.UrbanRoutesPage.card_code_field).send_keys(data.card_code)
        time.sleep(1)

        self.driver.find_element(*locators.UrbanRoutesPage.card_blank_field).click()
        time.sleep(1)

        self.driver.find_element(*locators.UrbanRoutesPage.card_summit_button).click()
        time.sleep(1)

        self.driver.find_element(*locators.UrbanRoutesPage.payment_method_close_button).click()
        time.sleep(1)

    def get_payment(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.pp_value_text).text


    def set_message(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(locators.UrbanRoutesPage.comment_field))

        self.driver.find_element(*locators.UrbanRoutesPage.comment_field).send_keys(data.message_for_driver)
        time.sleep(1)

    def get_message(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.comment_field).get_attribute('value')

    def set_requirements(self):
        #Open requirements
        self.driver.find_element(*locators.UrbanRoutesPage.requirements_dropdown).click()
        time.sleep(1)
        self.driver.find_element(*locators.UrbanRoutesPage.requirements_dropdown).click()
        #Manta y pan;uelos
        time.sleep(1)
        self.driver.find_element(*locators.UrbanRoutesPage.manta_panuelos_slider).click()
        time.sleep(1)
        #Pendiente ingresar asserts para verificar que el slide esta activo y el hlado se haya agregado
        self.driver.find_element(*locators.UrbanRoutesPage.helado_plus_button).click()
        time.sleep(1)
        self.driver.find_element(*locators.UrbanRoutesPage.helado_plus_button).click()
        time.sleep(1)

    def get_helado_counter(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.helado_counter_value_2).text

    def get_slider_status(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.manta_panuelos_check).is_selected()

    def call_taxi(self):
        self.driver.find_element(*locators.UrbanRoutesPage.call_taxi_button).click()

    def wait_driver_details(self):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.driver_order_details))

    def get_order_header_title(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.order_header_title).text