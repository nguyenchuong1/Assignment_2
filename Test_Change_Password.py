import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Đảm bảo ChromeDriver đã có trong PATH hoặc cung cấp đường dẫn chính xác
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
    driver.find_element(By.LINK_TEXT, "Tài khoản").click()
    time.sleep(1)
    assert "http://localhost/B08/index.php?quanly=thaydoimatkhau" in driver.current_url

def test_changepassfail(driver):
    # Mở trang đăng ký
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
    driver.find_element(By.LINK_TEXT, "Tài khoản").click()
    time.sleep(1)
    # Điền thông tin vào các trường nhập liệu
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[7]/td[2]/input").clear()
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[7]/td[2]/input").send_keys("kimanh@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div/form/table/tbody/tr[9]/td[2]/input").send_keys("12345")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div/form/table/tbody/tr[10]/td[2]/input").send_keys("12345")
    time.sleep(1)

    # Nhấn vào nút thay đổi
    change_button = driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[11]/td/input")
    change_button.click()

    # Đợi 2 giây để trang load (có thể điều chỉnh nếu cần)
    time.sleep(2)

    # Kiểm tra thông báo thay đổi thành công
    success_message = driver.find_element(By.XPATH, "/html/body/p").text
    assert success_message == "Tài khoản hoặc mật khẩu không đúng, vui lòng nhập lại!"



    time.sleep(3)


def test_changepass(driver):
    # Mở trang đăng ký
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
    driver.find_element(By.LINK_TEXT, "Tài khoản").click()
    time.sleep(1)
    # Điền thông tin vào các trường nhập liệu
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[7]/td[2]/input").clear()
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[7]/td[2]/input").send_keys("kimanh@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div/form/table/tbody/tr[9]/td[2]/input").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div/form/table/tbody/tr[10]/td[2]/input").send_keys("123456")
    time.sleep(1)

    # Nhấn vào nút thay đổi
    change_button = driver.find_element(By.XPATH, "/html/body/section[3]/div/div/form/table/tbody/tr[11]/td/input")
    change_button.click()

    # Đợi 2 giây để trang load (có thể điều chỉnh nếu cần)
    time.sleep(2)

    # Kiểm tra thông báo thay đổi thành công
    success_message = driver.find_element(By.XPATH, "/html/body/p").text
    assert success_message == "Tài khoản đã cập nhật!"



    time.sleep(3)



