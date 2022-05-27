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
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

chromeDriverPath = Service("D:\\EstudioDesarrollo\\Python\\practica-testing-python\\pythonSelenium\\Librerias\\chromedriver.exe")
driver = webdriver.Chrome(service=chromeDriverPath, chrome_options=options)
driver.maximize_window()


def open_page(page):
    # Inicializamos el navegador
    driver.get(page)


def set_data_by_css(path, text):
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, path)))\
        .send_keys(text)


def set_data_by_xpath(path, text):
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, path)))\
        .send_keys(text)


def clic_button_by_css(path):
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, path)))\
        .click()


def clic_button_by_xpath(path):
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, path)))\
        .click()
    time.sleep(1)


def close_driver():
    driver.close()


def get_text_by_css(path):
    text_colum = WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, path)))
    return text_colum.text


def get_text_by_xpath(path):
    text_colum = WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, path)))
    return text_colum.text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Abrimos Página Web
    open_page('https://www.facebook.com/')
    # Añadimos el correo
    set_data_by_css("#email", "")
    # Añadimos la contraseña
    set_data_by_css("#pass", "")
    # Presionamos el botón Iniciar Sesión
    clic_button_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
    # Presionamos el botón de notificaciones
    clic_button_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div[3]/span/div/span/div/a')
    # Presionamos el botón de menú dentro de notificaciones
    clic_button_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div')
    # Presionamos el botón de marcar todas como leidas
    clic_button_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div')
    # Presionamos el botón Menú cerrar sesión
    clic_button_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div[1]/div/div[1]/span/div/div[2]")
    # Presionamos la acción cerrar sesión
    clic_button_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[1]/div[2]/div/div[5]/div")

