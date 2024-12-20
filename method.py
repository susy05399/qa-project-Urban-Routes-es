from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import data
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
        from_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators.UrbanRoutesPage.from_field))
        from_field.clear()
        from_field.send_keys(address_from)

    def set_to(self, to_address):
        to_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators.UrbanRoutesPage.to_field))
        to_field.clear()
        to_field.send_keys(to_address)

    def request_taxi(self):
        taxi_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.taxi_button))
        taxi_button.click()

    def pick_comfort(self):
        comfort_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.comfort))
        comfort_button.click()

    def set_phone_number(self):
        phone_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.phone_field))
        phone_field.click()

        phone_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators.UrbanRoutesPage.phone_field_popup))
        phone_popup.clear()
        phone_popup.send_keys(data.phone_number)

        phone_submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.phone_summit_button))
        phone_submit_button.click()

        code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators.UrbanRoutesPage.code_field))
        code_field.clear()
        code_field.send_keys(retrieve_phone_code(self.driver))

        code_submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.code_summit_button))
        code_submit_button.click()

    def set_payment(self):
        payment_method_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.payment_method_field))
        payment_method_field.click()

        add_card_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.add_card))
        add_card_button.click()

        card_number_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locators.UrbanRoutesPage.card_number_field))
        card_number_field.clear()
        card_number_field.send_keys(data.card_number)

        card_code_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input.card-input#code")))  # Usando CSS Selector
        card_code_field.clear()
        card_code_field.send_keys(data.card_code)

        blank_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.card_blank_field))
        blank_field.click()

        card_submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.card_summit_button))
        card_submit_button.click()

        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.payment_method_close_button))
        close_button.click()

    def set_requirements(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.requirements_dropdown))
        dropdown.click()

        manta_panuelos_slider = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.manta_panuelos_slider))
        manta_panuelos_slider.click()

        helado_plus_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.helado_plus_button))
        helado_plus_button.click()
        helado_plus_button.click()

    def call_taxi(self):
        call_taxi_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locators.UrbanRoutesPage.call_taxi_button))
        call_taxi_button.click()

    def wait_driver_details(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(locators.UrbanRoutesPage.driver_order_details))