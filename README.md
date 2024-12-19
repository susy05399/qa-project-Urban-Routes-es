Proyecto de Automatización de Solicitud de Taxi Comfort

*Datos del creador:*

- Nombre: Susana Pérez Aparicio

- Grupo: No. 17

*Pasos para ejecutar el código:*

- Inicia sesión y conéctate a GitHub.
- Clona el repositorio en tu computadora.
- Instala Selenium en PyCharm desde la terminal.
- Instala Pytest en PyCharm desde la terminal.
- Si no cuentas con Google Chrome en tu computadora, procede a instalarlo.
- Ejecuta las pruebas de la aplicación Urban Routes con el siguiente comando bash:

      pytest /sprint_8/test.py

    O tambien por el contrario, puedes ejecutarlo desde PyCharm entrando a la carpeta de "test.py", dando clic en "Current File"
en la "v", seleccionando la flecha verde (Run 'test.py'') de la sección Current File.

*Herramientas de uso:*

- GitHub
- PyCharm
- Plataforma de TripleTen (enlace al servidor privado)
- GoogleChrome

*Funcionalidad:*

Este proyecto se centra en la automatización del proceso de solicitud de un taxi con la tarifa Comfort. Incluye un conjunto de pruebas para verificar la correcta implementación del proceso.

*Archivos del proyecto:*

- data.py: Contiene los valores de prueba que se utilizan en las pruebas automatizadas.
- locators.py: Define los localizadores necesarios para la automatización.
- method.py: Proporciona los métodos auxiliares usados en las pruebas.

*Pruebas de automatización:*

El proyecto se divide en un total de 8 pruebas automatizadas, cada una abordando diferentes aspectos del proceso:

- def test_set_route(self): Configura y verifica la configuración de la ruta.
- def test_pick_comfort(self): Selecciona y valida la tarifa Comfort.
- def test_set_phone_number(self): Ingresa y comprueba la introducción del número de teléfono.
- def test_set_payment(self): Ejecuta y revisa la configuración de los métodos de pago.
- def test_set_message(self): Ingresa y confirma la inclusión de un mensaje personalizado.
- def test_set_requirements(self): Configura y valida los requisitos adicionales.
- def test_call_taxi(self): Realiza la solicitud del taxi y verifica que la orden se haya ejecutado correctamente.
- def test_wait_driver_details(self): Verifica la recepción de los detalles del conductor y que el viaje haya sido aceptado.

*Para realizar la ejecución de las pruebas:*

1. Asegúrate de tener configurado e instalado Python.
2. Tener instalado Selenium. 
    
   
- Para instalar Selenium lo puedes hacer desde la terminal usando el siguiente código: 

       pip install selenium
3. Instalar y ejecutar las pruebas con Pytest.

- Para instalar Pytest lo puedes hacer desde la terminal usando el siguiente código:

        pip install pytest

Nota: Las pruebas se realizan sobre Google Chrome. Asegúrate de tener la versión adecuada de Google Chrome Driver (la más reciente). 

Tampoco olvides mantener actualizado el enlace proporcionado por la plataforma privada de TripleTen, ya que este caduca después de un tiempo.