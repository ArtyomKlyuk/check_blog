from Auths import gmail, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def auth_pro_culture():
    gmail = 'Artem.Kluykovskiy@fabit.ru'
    password = 'Fakemask01'
    driver.get('https://pro.culture.ru/new/auth/login')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "ant-input").send_keys(gmail)
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME, 'ant-input')[1].send_keys(password)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,
                        ".ant-btn.ant-btn-primary").click()
    time.sleep(4)
    driver.find_element(By.CSS_SELECTOR, ".main-form_organization-link").click()
    time.sleep(3)
