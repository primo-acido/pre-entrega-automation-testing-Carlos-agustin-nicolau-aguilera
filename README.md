# 🧪 Proyecto de Automatización - SauceDemo con Selenium y Pytest

Este proyecto tiene como objetivo **automatizar pruebas funcionales web** sobre el sitio de práctica (https://www.saucedemo.com/) utilizando **Python, Selenium y Pytest**.  
Las pruebas automatizan casos básicos como el **inicio de sesión**, la **verificación de catálogo de productos** y la **interacción con el carrito de compras**.

---

## 🎯 Propósito del proyecto

El propósito principal de este proyecto es poner en práctica los fundamentos del **Testing Automatizado con Selenium WebDriver**, aplicando buenas prácticas en la estructura de carpetas, uso de *fixtures* y ejecución de pruebas con Pytest.

Entre los objetivos específicos se incluyen:

- Automatizar el acceso y login en el sitio **SauceDemo**.  
- Validar la carga del catálogo de productos.  
- Verificar la funcionalidad del carrito de compras (agregar artículos y validar el contador).  
- Aprender a organizar un proyecto de testing con `pytest` y `webdriver_manager`.

---

## 🧰 Tecnologías utilizadas

- **Python 3.13**
- **Selenium 4.x**
- **Pytest 8.x**
- **WebDriver Manager** (para gestionar automáticamente el driver de Chrome)
- **Google Chrome** (como navegador principal)

---

## ⚙️ Instalación de dependencias

Antes de ejecutar el proyecto, asegúrate de tener instalado **Python 3.10 o superior** y **pip**.

 pip install selenium webdriver-manager pytest



## ▶️ Ejecución de las pruebas
 
Una vez instaladas las dependencias, puedes ejecutar las pruebas con el siguiente comando desde la raíz del proyecto:

bash
pytest -v
🔹 -v (verbose) muestra el resultado detallado de cada test.
🔹 Puedes generar un reporte HTML si tienes instalado pytest-html:

bash
pytest --html=report.html --self-contained-html
Esto creará un archivo report.html con el resumen de ejecución.