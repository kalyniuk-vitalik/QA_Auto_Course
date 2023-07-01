import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

firefox = webdriver.Firefox()
firefox.get("https://stepik.org/lesson/236895/step/1")


driver.get("https://stepik.org/lesson/236895/step/1")


wait = WebDriverWait(driver, 10)

signin_element = wait.until(EC.visibility_of_element_located((By.ID, "ember33")))
signin_element.click()

#email_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='login']")))
email_field = driver.find_element(By.CSS_SELECTOR, "input[name='login']")
email_field.send_keys("vitalik1802@gmail.com")

#password_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
password_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password_field.send_keys("Vitalik1992")

login_button = driver.find_element(By.CLASS_NAME, "sign-form__btn")
login_button.click()
time.sleep(10)

