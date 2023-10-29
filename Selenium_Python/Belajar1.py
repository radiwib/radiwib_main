from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/automation-practice-form")
time.sleep(1)


def demoqa_form():
    driver.maximize_window()
    driver.find_element(By.ID, 'firstName').click()
    driver.find_element(By.ID, 'firstName').send_keys('Rahadian')
    time.sleep(2)

    driver.find_element(By.ID, 'lastName').click()
    driver.find_element(By.ID, 'lastName').send_keys('Wibisono')
    time.sleep(2)

    driver.find_element(By.ID, 'userEmail').click()
    driver.find_element(By.ID, 'userEmail').send_keys('radi.wib@gmail.com')
    time.sleep(2)

    driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()
    time.sleep(2)

    driver.find_element(By.ID, 'userNumber').click()
    driver.find_element(By.ID, 'userNumber').send_keys('112233445566')
    time.sleep(2)

    driver.find_element(By.ID, 'dateOfBirthInput').click()
    pyautogui.doubleClick
    pyautogui.press('backspace', presses=1)
    time.sleep(2)
    driver.find_element(By.ID, 'dateOfBirthInput').send_keys('29 Nov 2021')

demoqa_form()
