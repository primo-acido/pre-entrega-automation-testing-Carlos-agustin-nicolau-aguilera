import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo, get_driver


@pytest.fixture
def driver():
    # configuracion para consultar a selenium web driver

    driver = get_driver()
    yield driver
    driver.quit()



def test_login(driver):


    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'
    #assert
    #logueo de usuario con username y password
    #click al boton de login

    #redirige a la pagina de inventario

    #verificar el titulo de la pagina (ventanita)
    

def test_catalogo(driver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0


    #logueo de usuario con username y password
    #click al boton de login

    #podamos verificar el titulo pero del html

    #Comprobar si existen productos en la pagina visibles
    


def test_carrito(driver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    total_products = len(products)

    if total_products >= 2:
        products[0].find_element(By.TAG_NAME, 'button').click()
        products[1].find_element(By.TAG_NAME, 'button').click()

        badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert badge == "2"

    
    #logueo de usuario con username y password
    #click al boton de login
    #llevarme al carrito de compras
    #incremento al agregar productos al carrito
    #comprobar que el carrito aparezca el producto correcto
    
    
