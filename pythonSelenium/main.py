# Librerias
# Web Driver Selenium: https://chromedriver.chromium.org/
import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

chromeDriverPath = Service("D:\\EstudioDesarrollo\\Python\\practica-testing-python\\pythonSelenium\\Librerias\\chromedriver.exe")
driver = webdriver.Chrome(service=chromeDriverPath, chrome_options=options)
driver.maximize_window()


def open_youtube():
    # Inicializamos el navegador
    driver.get('https://www.youtube.com/')


def set_data(selector, text):
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))\
        .send_keys(text)


def clic_button(selector):
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))\
        .click()


def xpath_select_option(path):
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, path)))\
        .click()


def close_driver():
    driver.close()


def buscar_cancion(cancion):
    # Buscamos una canción
    set_data('input#search', cancion)
    # Deplay
    time.sleep(1)
    # Buscamos la canción
    clic_button("#search-icon-legacy")


def seleccionar_cancion(opcion):
    # Seleccionamos una canción
    spath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[" \
            "1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[" \
            "2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[" + opcion + "]/div[1]/ytd-thumbnail/a "
    xpath_select_option(spath)


def obtener_titulo():
    path = '#container > h1 > yt-formatted-string'
    text_colum = WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, path)))
    return text_colum.text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Abrimos youtube
    open_youtube()
    #Buscamos una cación
    buscar_cancion('hello')
    # Reproducimos el primer item que nos aparece
    seleccionar_cancion('1')
    # Obtener Titulo
    title = obtener_titulo()
    print("El titulo del video es: ", title)
    # Cerrar Navegador
    close_driver()
