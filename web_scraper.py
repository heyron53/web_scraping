

# import requests

from bs4 import BeautifulSoup
from pprint import pprint

# Selenium permite realizar peticiones con tiempo de espera, de esta forma evadimos el js
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options # Por defecto abrimos un navegador, con Options podemos restringirlo


for page_num in range(1,10):

    # Para esta prueba se ha realizado en la Wipoid.com
    url = f"https://www.wipoid.com/tarjetas-graficas-nvidia/#/page-{page_num}"

    # Restringimos que se abra una ventana
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options = chrome_options)


    with driver.get(url) as driver:

        print(f"PAGINA: {page_num}")
        print(f"URL: {url}")

        wait = WebDriverWait(driver, 10)  
        page_source = driver.page_source # Recogemos el contenido

        soup = BeautifulSoup(page_source, "html.parser")
        products = soup.findAll("div", {"class", "block-product-inner"})

        for product in products:

            title = product.find("a", {"class", "product-name"}).getText(strip=True) # strip = True para evitar carácteres extras
            pprint(title)

        driver.quit() # Cerramos la petición
 

