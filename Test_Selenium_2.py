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
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng xuất").click()
    time.sleep(1)
    assert 'http://localhost/B08/index.php?dangxuat=1' in driver.current_url

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
#test navigation
def test_navigation_bar_not_login(driver):
    driver.get("http://localhost/B08/index.php")  
    # Nhập từ khóa chữ thường và thực hiện tìm kiếm
    buttons = [
    "/html/body/section[1]/header/div/div/div[3]/ul/li[2]/a",  # Trang chủ
    "/html/body/section[1]/header/div/div/div[3]/ul/li[3]/a",  # Thực đơn
    "/html/body/section[1]/header/div/div/div[3]/ul/li[4]/a",  # Liên hệ
    "/html/body/section[1]/header/div/div/div[3]/ul/li[5]/a"  # Cart  
]

# Danh sách để lưu các nút không truy cập được và các nút truy cập thành công
    failed_buttons = []
    accessed_buttons = []

    for xpath in buttons:
        try:
            # Mở menu nếu cần thiết
            driver.find_element(By.CLASS_NAME, "menu-bar").click()
            time.sleep(1)
            
            # Lấy tên của nút và nhấn vào nó
            button_element = driver.find_element(By.XPATH, xpath)
            name = button_element.text
            button_element.click()
            time.sleep(2)
            
            # Kiểm tra trang lỗi 404 bằng cách tìm thông báo lỗi
            try:
                error_text = driver.find_element(By.XPATH, "/html/body/p").text
                if error_text == "The requested URL was not found on this server.":
                    failed_buttons.append(name)
                    driver.back()
                    time.sleep(2)
                else:
                    accessed_buttons.append(name)
            except:
                # Nếu không tìm thấy trang lỗi 404, thì nút này truy cập thành công
                accessed_buttons.append(name)
        except Exception as e:
            # Nếu có lỗi trong quá trình tìm kiếm hoặc nhấn vào nút, lưu nút vào danh sách failed_buttons
            failed_buttons.append((name, str(e)))

    # In kết quả sau khi kiểm tra tất cả các nút
    print("Các nút không truy cập được:")
    for button in failed_buttons:
        print(f"Nút: {button}")

    print("\nCác nút truy cập thành công:")
    for button in accessed_buttons:
        print(f"Nút: {button}")
    assert "http://localhost/B08/index.php?quanly=giohang" in driver.current_url
def test_navigation_bar_login(driver): # cái này sau khi login rồi
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
    
    # Nhập từ khóa chữ thường và thực hiện tìm kiếm
    buttons = [
    "/html/body/section[1]/header/div/div/div[3]/ul/li[2]/a",  # Trang chủ
    "/html/body/section[1]/header/div/div/div[3]/ul/li[3]/a",  # Thực đơn
    "/html/body/section[1]/header/div/div/div[3]/ul/li[4]/a",  # Liên hệ
    "/html/body/section[1]/header/div/div/div[3]/ul/li[5]/a",  #Cart
    "/html/body/section[1]/header/div/div/div[3]/ul/li[6]/a"  # Tài khoản  
]

# Danh sách để lưu các nút không truy cập được và các nút truy cập thành công
    failed_buttons = []
    accessed_buttons = []

    for xpath in buttons:
        try:
            # Mở menu nếu cần thiết
            driver.find_element(By.CLASS_NAME, "menu-bar").click()
            time.sleep(1)
            
            # Lấy tên của nút và nhấn vào nó
            button_element = driver.find_element(By.XPATH, xpath)
            name = button_element.text
            time.sleep(1)
            button_element.click()
            time.sleep(2)
            
            # Kiểm tra trang lỗi 404 bằng cách tìm thông báo lỗi
            try:
                error_text = driver.find_element(By.XPATH, "/html/body/p").text
                if error_text == "The requested URL was not found on this server.":
                    failed_buttons.append(name)
                    driver.back()
                    time.sleep(2)
                else:
                    accessed_buttons.append(name)
            except:
                # Nếu không tìm thấy trang lỗi 404, thì nút này truy cập thành công
                accessed_buttons.append(name)
        except Exception as e:
            # Nếu có lỗi trong quá trình tìm kiếm hoặc nhấn vào nút, lưu nút vào danh sách failed_buttons
            failed_buttons.append((name, str(e)))

    # In kết quả sau khi kiểm tra tất cả các nút
    print("Các nút không truy cập được:")
    for button in failed_buttons:
        print(f"Nút: {button}")

    print("\nCác nút truy cập thành công:")
    for button in accessed_buttons:
        print(f"Nút: {button}")
    assert "http://localhost/B08/index.php?quanly=thaydoimatkhau" in driver.current_url
