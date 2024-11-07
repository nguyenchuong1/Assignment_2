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
# Test function search
def test_valid_search(driver):
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[1]").send_keys("Caramel")  # search name item
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[2]").click()
    time.sleep(1)
    products = driver.find_elements(By.CLASS_NAME, "item")
    assert len(products) > 0, "Không tìm thấy sản phẩm nào trong kết quả tìm kiếm"
def test_unvalid_search(driver): # ex:caramel@#$% , HJKHKJh
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[1]").send_keys("Caramel@#$")  # search name item
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[2]").click()
    time.sleep(1)
    result = driver.find_element(By.XPATH, "/html/body/section[3]/div/div/div/p").text
    time.sleep(1)
    assert 'Không tìm thấy kết quả' in result
def test_empty_search(driver): # không nhập gì
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[2]").click()
    time.sleep(1)
    search_input = driver.find_element(By.ID, "search-text")
    # Kiểm tra thông báo từ custom validity message
    custom_message = search_input.get_attribute("validationMessage")
    assert "Vui lòng người dùng nhập từ khóa tìm kiếm!" in custom_message, "Thông báo không đúng"
    driver.quit()
def test_case_insensitive_search(driver):
    driver.get("http://localhost/B08/index.php")
    
    # Nhập từ khóa chữ thường và thực hiện tìm kiếm
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[1]").send_keys("trà")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[2]").click()
    time.sleep(1)
    # Lấy danh sách kết quả cho từ khóa chữ thường
    results_lowercase = driver.find_elements(By.CLASS_NAME, "item")
    results_text_lowercase = [result.text for result in results_lowercase]  # Lưu danh sách văn bản của các kết quả

    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[1]").send_keys("TRÀ")
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[2]").click()
    time.sleep(1)      
    # Lấy danh sách kết quả cho từ khóa chữ hoa
    results_uppercase = driver.find_elements(By.CLASS_NAME, "item")
    results_text_uppercase = [result.text for result in results_uppercase]  # Lưu danh sách văn bản của các kết quả
    # So sánh kết quả từ hai tìm kiếm
    assert results_text_lowercase == results_text_uppercase, "Kết quả tìm kiếm không khớp giữa chữ hoa và chữ thường"
