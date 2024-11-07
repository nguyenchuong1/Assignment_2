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
def test_navigation_main_bar_not_login(driver):
    driver.get("http://localhost/B08/index.php")  
    # Nhập từ khóa chữ thường và thực hiện tìm kiếm
    buttons = [
    "/html/body/section[1]/header/div/div/div[3]/ul/li[2]/a",  # Trang chủ
    "/html/body/section[1]/header/div/div/div[3]/ul/li[3]/a",  # Thực đơn
    "/html/body/section[1]/header/div/div/div[3]/ul/li[4]/a",  # Liên hệ
    "/html/body/section[1]/header/div/div/div[3]/ul/li[5]/a"  # Cart  
]



    for xpath in buttons:
     
            # Mở menu nếu cần thiết
            driver.find_element(By.CLASS_NAME, "menu-bar").click()
            time.sleep(1)
            
            # Lấy tên của nút và nhấn vào nó
            button_element = driver.find_element(By.XPATH, xpath)
            name = button_element.text
            button_element.click()
            time.sleep(2)
            

    
    assert "http://localhost/B08/index.php?quanly=giohang" in driver.current_url
def test_navigation_main_bar_login(driver): # cái này sau khi login rồi
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
    

    for xpath in buttons:
    
            # Mở menu nếu cần thiết
        driver.find_element(By.CLASS_NAME, "menu-bar").click()
        time.sleep(1)
            
            # Lấy tên của nút và nhấn vào nó
        button_element = driver.find_element(By.XPATH, xpath)
        time.sleep(1)
        button_element.click()
        time.sleep(2)
       
    assert "http://localhost/B08/index.php?quanly=thaydoimatkhau" in driver.current_url

def test_navigation_icon(driver):
    driver.get("http://localhost/B08/index.php")  
    
    button_element = driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[1]/a/img")
    button_element.click()
    time.sleep(2)
    assert "http://localhost/B08/index.php" in driver.current_url
    driver.back()    
    time.sleep(2)
    
    button_element = driver.find_element(By.XPATH, "/html/body/section[4]/div/div[2]/a[1]")
    button_element.click()
    time.sleep(2)
    driver.back()    
    time.sleep(2)
    assert "https://www.facebook.com/nguyenchuong010866az" in driver.current_url    
    button_element = driver.find_element(By.XPATH, "/html/body/section[4]/div/div[2]/a[2]")
    button_element.click()
    time.sleep(2)
    assert "https://www.X.com/nguyenchuong010866az/" in driver.current_url
    driver.back()    
    time.sleep(2)
    
    button_element = driver.find_element(By.XPATH, "/html/body/section[4]/div/div[2]/a[3]")
    button_element.click()
    time.sleep(2)
    assert "https://www.instagram.com/nguyenchuong010866az/" in driver.current_url
    driver.back()    
    time.sleep(2)
    
    
 
def test_menu_category_navigation(driver): # kiểm tra danh mục của thực đơn có chuyển trang từng loại không 
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[3]/div/nav/ul/li[1]/a").click()
    time.sleep(1)
    assert "http://localhost/B08/index.php?quanly=menu&id=2" in driver.current_url
    driver.find_element(By.XPATH, "/html/body/section[3]/div/nav/ul/li[2]/a").click()
    time.sleep(1)
    assert "http://localhost/B08/index.php?quanly=menu&id=1" in driver.current_url

    
