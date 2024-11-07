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
def test_login_to_Account_page(driver):
    driver.get("http://localhost/B08/index.php") # hàm này để đã login và đặt sản phẩm vô được
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("123456")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[6]/a").click()
    time.sleep(1)
    assert "http://localhost/B08/index.php?quanly=thaydoimatkhau" in driver.current_url
def test_login_to_Account_page_fail(driver):
    driver.get("http://localhost/B08/index.php") # hàm này để đã login và đặt sản phẩm vô được
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("123456")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[6]/a").click()
    time.sleep(1)
    # Điền thông tin vào các trường nhập liệu
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[7]/td[2]/input").clear()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[7]/td[2]/input").send_keys("nguyenchuoing@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div/form/table/tbody/tr[9]/td[2]/input").send_keys("1234")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div/form/table/tbody/tr[10]/td[2]/input").send_keys("123456")
    time.sleep(1)
    # Nhấn vào nút thay đổi
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[11]/td/input").click()
    time.sleep(2)
    error_message = driver.find_element(By.XPATH, "/html/body/p").text
    assert  "Tài khoản hoặc mật khẩu không đúng, vui lòng nhập lại!" in error_message
    time.sleep(1)
 
def test_login_to_Account_page_pass(driver):
    driver.get("http://localhost/B08/index.php") # hàm này để đã login và đặt sản phẩm vô được
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("123456")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[6]/a").click()
    time.sleep(1)
    # Điền thông tin vào các trường nhập liệu
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[7]/td[2]/input").clear()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[7]/td[2]/input").send_keys("kimanhtran@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div/form/table/tbody/tr[9]/td[2]/input").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div/form/table/tbody/tr[10]/td[2]/input").send_keys("123456789")
    time.sleep(1)
    # Nhấn vào nút thay đổi
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[11]/td/input").click()
    time.sleep(1)
    success_message = driver.find_element(By.XPATH, "/html/body/p").text
    time.sleep(1)
    assert  "Tài khoản đã cập nhật!" in success_message
    



