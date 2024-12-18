Proyecto de Automatización de Solicitud de Taxi Comfort

Datos del creador: 
- Nombre: "Susana Pérez Aparicio".
- Grupo: no.17

Instalación:

1. Inicia sesión y conectate a GitHub;
2. Clona el repositorio en tu computadora;
3. Instala Selenium en PyCharm desde la terminal; 
4. Instala Pytest en PyCharm desde la terminal; 
5. Si no cuentas con GoogleChrome en tu computadora, procede a instalarlo; 
6. Ejecuta las pruebas de la aplicación Urban Routes con el siguiente comando:
pytest /sprint_8/test.py


Herramientas de uso:

1. Github
2. PyCharm
3. Plataforma de TripleTen (Link del servidor privado)

Funcionalidad:

Este proyecto se centra en la automatización del proceso de solicitar un taxi con la tarifa Comfort. Se incluye un conjunto de pruebas para verificar la correcta implementación del proceso mismo.

Archivos del Proyecto:

data.py: Contiene los valores de prueba que se utilizan en las pruebas automatizadas.
locators.py: Define los localizadores necesarios para la automatización.
method.py: Proporciona los métodos auxiliares usados en las pruebas. 

Pruebas de Automatización.

El proyecto se divide en un total de 8 pruebas automatizadas, cada una abordando diferentes aspectos del proceso:

def test_set_route(self): Configura y verifica la configuración de la ruta.
def test_pick_comfort(self): Selecciona y valida la selección de la tarifa Comfort.
def test_set_phone_number(self): Ingresa y comprueba la introducción del número de teléfono.
def test_set_payment(self): Ejecuta y revisa la configuración de los métodos de pago.
def test_set_message(self): Ingresa y confirma la inclusión de un mensaje personalizado.
def test_set_requirements(self): Setea y valida la configuración de los requisitos adicionales.
def test_call_taxi(self): Realiza la llamada al taxi y se verifica que se haya ejecutado la orden.
def test_wait_driver_details(self): Verifica la recepción de los detalles del conductor y que el viaje haya sido tomado.

Para realizar la ejecución de las Pruebas:

- Asegúrate de tener configurado e instalado Python
- Tener instalado Selenium
- Instalar y ejecutar las pruebas con pytest.

Nota: Las pruebas se realizan sobre GoogleChrom, asegurate de tener la version adecuada de GoogleChromeDriver (la mas reciente)

