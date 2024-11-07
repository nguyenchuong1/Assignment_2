import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# User Authentication
# TC1: Valid Login
# TC2: Invalid Login
# TC3: Empty Username/Password
# TC4: Logout Functionality

# Test function login/logout 
def test_valid_login(driver): # nhập đúng login
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong")  # Username
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("123456")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(2)
    assert "http://localhost/B08/index.php" in driver.current_url

def test_unvalid_login(driver): # nhập sai login
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong")  # Username
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("123445656")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(2) 
    mess_error = driver.find_element(By.XPATH, "/html/body/p").text
    assert 'Tài khoản hoặc mật khẩu không đúng, vui lòng nhập lại!' in mess_error
    time.sleep(2) 
def test_logout(driver): # thoát ra 
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong")  # Username
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("123456")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng xuất").click()
    time.sleep(1)
    assert 'http://localhost/B08/index.php?dangxuat=1' in driver.current_url
