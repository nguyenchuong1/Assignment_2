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


# Test function Register
def test_register(driver):
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, " /html/body/div/form/div[5]/a[2]").click()  
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong696969")  # Username
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("Nguyen Hoang Chuong")  # Họ tên
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys("12345678")  # pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys("12345678")  # nhập lại pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[8]/input").send_keys("chuong69@gmail.com")  # email
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[9]/input").send_keys("0934010866")  # sdt
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/input[2]").click() # nhấn nút
    time.sleep(5)
    assert "http://localhost/B08/login.php" in driver.current_url

def test_empty_register(driver):
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, " /html/body/div/form/div[5]/a[2]").click()  
    time.sleep(1)
    
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/input[2]").click() # nhấn nút
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "vui lòng nhập tên đăng nhập !"  # Kiểm tra nội dung
    alert.accept() 
    
def Test_registration_username_already_exists(driver):
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, " /html/body/div/form/div[5]/a[2]").click()  
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong696969")  # Username
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("Nguyen Hoang Chuong")  # Họ tên
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys("12345678")  # pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys("12345678")  # nhập lại pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[8]/input").send_keys("chuong69@gmail.com")  # email
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[9]/input").send_keys("0934010866")  # sdt
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/input[2]").click() # nhấn nút
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Tài khoản đã tồn tại, vui lòng chọn tên đăng nhập khác."  # Kiểm tra nội dung
    alert.accept() 

def test_wrong_password_re_enter(driver):
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, " /html/body/div/form/div[5]/a[2]").click()  
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong696969")  # Username
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("Nguyen Hoang Chuong")  # Họ tên
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys("12345678")  # pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys("87654321")  # nhập lại pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[8]/input").send_keys("chuong69@gmail.com")  # email
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[9]/input").send_keys("0934010866")  # sdt
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/input[2]").click() # nhấn nút
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Mật khẩu nhập lại sai ! Vui lòng nhập lại!"  # Kiểm tra nội dung
    alert.accept() 

def test_name_have_special_characters(driver):
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, " /html/body/div/form/div[5]/a[2]").click()  
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong696969")  # Username
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("$@#$Nguyen Hoang Chuong@#")  # Họ tên
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys("12345678")  # pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys("87654321")  # nhập lại pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[8]/input").send_keys("chuong69@gmail.com")  # email
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[9]/input").send_keys("0934010866")  # sdt
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/input[2]").click() # nhấn nút
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Vui Lòng không nhập họ và tên bằng kí tự đặc biệt!"  # Kiểm tra nội dung
    alert.accept() 

def test_number_phone__in_register(driver):
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, " /html/body/div/form/div[5]/a[2]").click()  
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong696969")  # Username
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("Nguyen Hoang Chuong")  # Họ tên
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys("12345678")  # pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys("12345678")  # nhập lại pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[8]/input").send_keys("chuong69@gmail.com")  # email
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[9]/input").send_keys("0934010866#$%")  # sdt
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/input[2]").click() # nhấn nút
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Số điện thoại chỉ được chứa các chữ số!"  # Kiểm tra nội dung
    alert.accept() 
def test_valid_email_in_register(driver):
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, " /html/body/div/form/div[5]/a[2]").click()  
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong696969")  # Username
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("Nguyen Hoang Chuong")  # Họ tên
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[3]/input").send_keys("12345678")  # pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[4]/input").send_keys("12345678")  # nhập lại pass
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[8]/input").send_keys("chuong69#gmail&com")  # email
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[9]/input").send_keys("0934010866")  # sdt
    time.sleep(1)
    
    driver.find_element(By.XPATH, "/html/body/div/form/input[2]").click() # nhấn nút
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Định dạng email không hợp lệ! Vui lòng nhập lại."  # Kiểm tra nội dung
    alert.accept() 
