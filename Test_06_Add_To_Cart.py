import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.alert import Alert
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
#1
def test_empty_cart_logged(driver):  # giỏ hàng rỗng
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("123456")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[1]/header/div/div/div[3]/ul/li[5]/a/i").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/form/table/tbody/tr[8]/th/input").click()
    # Chờ cho alert xuất hiện và kiểm tra nội dung
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(1)
    # Xác minh nội dung của alert
    assert alert.text == "Vui lòng điền đầy đủ thông tin và thêm sản phẩm vào giỏ hàng trước khi thanh toán."
    
    # Đóng alert sau khi xác minh
    alert.accept()
    
    # Kiểm tra điều hướng đến trang giỏ hàng
    assert driver.current_url == "http://localhost/B08/index.php?quanly=giohang"
#2
def test_add_to_cart_not_login(driver):  # thêm sản phẩm vào giỏ hàng khi chưa đăng nhập
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click() # chọn hình 3 sọc ngang ở trên góc phải 
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[3]/a").click() # chọn thực đơn
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[4]/div/div/div[2]/div[1]/div[2]/a/input").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
    time.sleep(1)
    assert driver.current_url == "http://localhost/B08/login.php"
#3
def test_add_to_cart_logged(driver): 
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
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click() # nút thêm vào giỏ hàng
    time.sleep(1)
    cart_items = driver.find_elements(By.XPATH, "//tbody[@id='giohang']/tr")
    time.sleep(1)
    assert len(cart_items)>0
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[3]/div/form/table/tbody/tr[8]/th/input").click()
    time.sleep(3)
    p = driver.find_element(By.XPATH,"/html/body/div[1]/h2").text
    assert p == "Quý khách đặt hàng thành công,chúng tôi sẽ liên hệ với quý khách sớm nhất"
#4
def test_add_to_cart_with_size_topping_and_quantity_before_add_to_cart(driver):
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
    
    # Chọn sản phẩm 
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(1)
    #chọn size
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div[1]/div[1]/input[3]").click()
    text_size = driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div[1]/div[1]/input[3]").get_attribute("value")
    time.sleep(1)
    #chọn topping
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div[1]/div[2]/input[1]").click()
    text_topping = driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div[1]/div[2]/input[1]").get_attribute("value")
    time.sleep(1)
    #chọn quantity
    input_element = driver.find_element(By.ID, "soluongdat")
    for _ in range(5):
        input_element.send_keys(Keys.ARROW_UP)
    text_quantity = driver.find_element(By.ID, "soluongdat").text
    time.sleep(1)
    #thêm sản phẩm vào cart
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
    time.sleep(2)

    test_col_topping = driver.find_element(By.XPATH,"/html/body/section[3]/div/table[1]/tbody[2]/tr/td[5]").text
    test_col_size = driver.find_element(By.XPATH,"/html/body/section[3]/div/table[1]/tbody[2]/tr/td[7]").text
    test_col_quantity = driver.find_element(By.XPATH,"/html/body/section[3]/div/table[1]/tbody[2]/tr/td[8]/input").text
    
    assert text_size == test_col_size
    assert test_col_topping.replace(",", "") == text_topping
    assert test_col_quantity == text_quantity
#5
def test_decrease_quantity_before_add_to_cart(driver):
    driver.get("http://localhost/B08/index.php") # hàm này để đã login và đặt sản phẩm vô được
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("123456")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click() #đăng nhập
    time.sleep(1)
    # Chọn sản phẩm
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(1)
    #chọn quantity
    input_element = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input")
    input_element.send_keys(Keys.ARROW_DOWN)
    
    # Lấy giá trị số lượng sau khi giảm
    text_quantity = input_element.get_attribute('value')
    time.sleep(2)
    
    # Kiểm tra giá trị số lượng
    assert text_quantity == "1"
#6
def test_invalid_quantity_input_before_add_to_cart(driver):
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
    # Chọn sản phẩm
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(1)
    #chọn quantity
    driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input").clear()
    input_element = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input").send_keys("0")
    quantity_alert = driver.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input")
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
    time.sleep(5)
    custom_message = quantity_alert.get_attribute("validationMessage")
    assert "Value must be greater than or equal to 1." in custom_message
    driver.quit()
# hàm được gọi
def get_all_products(driver):
    # Lấy tất cả các sản phẩm trên trang
    products = driver.find_elements(By.CSS_SELECTOR, '.list .item')
    return products
# hàm được gọi
def get_product_name(product):
    # Lấy tên sản phẩm từ mỗi item
    title = product.find_element(By.CSS_SELECTOR, '.title-item').text
    return title
#7
def test_random_product_add_to_cart(driver): #Hàm random 4 sản phẩm trong tất cả sản phẩm của web hiện có
    # Mở trang web
    driver.get("http://localhost/B08/index.php")
    
    # Tìm menu và nhấn vào Thực đơn
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Thực đơn").click()
    time.sleep(1)

    # Danh sách các xpath cho các danh mục cần lấy
    dm = ["/html/body/section[3]/div/nav/ul/li[1]/a",  # coffee
          "/html/body/section[3]/div/nav/ul/li[2]/a"]  # Trà sữa
    
    # Danh sách chứa tên các sản phẩm
    product_names = []

    # Lặp qua từng danh mục
    for dm_item in dm:
        try:
            # Click vào danh mục
            driver.find_element(By.XPATH, dm_item).click()
            time.sleep(2)  # Đợi trang tải sau khi click vào danh mục

            # Lấy tất cả các phần tử <a> trong danh sách phân trang
            page_links = driver.find_elements(By.CSS_SELECTOR, 'ul.listPage li a')
            
            # Lặp qua từng trang, click vào trang để lấy sản phẩm
            for i in range(len(page_links)):
                # Click vào liên kết trang
                page_links[i].click()
                time.sleep(2)  # Đợi trang tải sau khi click
                
                # Lấy tất cả sản phẩm trên trang hiện tại
                all_products = get_all_products(driver)
                
                # Lấy tên của tất cả sản phẩm và thêm vào danh sách
                for product in all_products:
                    product_names.append(get_product_name(product))
                
                # Kiểm tra URL sau khi chuyển trang (đảm bảo có tham số "trang")
                current_url = driver.current_url
                if "trang=" in current_url:
                    print(f"Đã chuyển đến trang: {current_url}")
                else:
                    print(f"Lỗi chuyển trang: {current_url}")
                
                # Sau khi click một trang, lấy lại các liên kết trang sau khi trang mới tải
                page_links = driver.find_elements(By.CSS_SELECTOR, 'ul.listPage li a')

        except Exception as e:
            print(f"Lỗi khi xử lý danh mục {dm_item}: {e}")

    
    random_products = random.sample(product_names, 4)

   
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("123456")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(2)
    for pd in random_products:
        driver.find_element(By.CLASS_NAME, "menu-bar").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[1]").send_keys(f"{pd}")  # search name item
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[2]").click()
        time.sleep(1)

        #chọn xem chi tiết sản phẩm:
        driver.find_element(By.XPATH, "/html/body/section[3]/div/div/div/div/div[2]/a/input").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
        time.sleep(1)
        assert "http://localhost/B08/index.php?quanly=giohang" in driver.current_url

    cart_items = driver.find_elements(By.XPATH, "//tbody[@id='giohang']/tr")
    time.sleep(1)
    assert len(cart_items)==4   
    # Đóng trình duyệt sau khi hoàn thành
    driver.quit()

#8 :xóa  sản phẩm trong cart
def test_remove_product_in_cart(driver):
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
    
    # Chọn sản phẩm
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(1)
    #thêm sản phẩm vào cart
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
    time.sleep(2)
    #Nhấn nút thùng rác để xóa sản phẩm ra khỏi cart
    driver.find_element(By.XPATH,"/html/body/section[3]/div/table[1]/tbody[2]/tr/td[10]/a/i").click()
    # kiểm tra số lượng sản phẩm trong cart
    cart_items = driver.find_elements(By.XPATH, "//tbody[@id='giohang']/tr")
    time.sleep(1)
    assert len(cart_items)==0
    time.sleep(1)

#9 Hủy đơn hàng
def test_cancel_order(driver):
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
    
    # Chọn sản phẩm
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(1)
    #thêm sản phẩm vào cart
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/section[3]/div/form/table/tbody/tr[8]/th/input").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[5]/a/i").click()
    time.sleep(1)
    #nhấn hủy đơn hàng
    driver.find_element(By.XPATH, "/html/body/section[3]/div/table[2]/tbody/tr[2]/td[13]/a").click()
    time.sleep(1)
    alert = Alert(driver)
    alert.accept()  # Bấm OK trong hộp thoại confirm

    time.sleep(2)
    status =  driver.find_element(By.XPATH, " /html/body/section[3]/div/table[2]/tbody/tr[2]/td[12]").text
    assert "Đơn hàng đã bị hủy" == status
    
#10 Kiểm tra khi đặt sản phẩm vượt quá số lượng mà web hiện có 
def test_order_product_beyond_existing_quantity(driver):
    driver.get("http://localhost/B08/index.php")  # Trang web đã login và thêm sản phẩm vào giỏ
    
    # Đăng nhập
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/form/div[1]/input").send_keys("chuong")  # Username
    driver.find_element(By.XPATH, "/html/body/div/form/div[2]/input").send_keys("123456")  # Password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "button").click()
    time.sleep(1)
    
    # Chọn sản phẩm
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    time.sleep(1)

    # Lấy số lượng hiện có của sản phẩm
    quantity_currently_available = int(driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/p[2]").text.split(":")[1].strip())
    time.sleep(1)
    
    # Gán số lượng vượt quá
    input_element = driver.find_element(By.ID, "soluongdat")
    input_element.clear()  # Đảm bảo ô input được xóa trước khi nhập
    input_element.send_keys(str(quantity_currently_available + 1))  # Gửi số lượng vượt quá vào ô input
    
    time.sleep(1)
    
    # Thêm sản phẩm vào giỏ hàng
    driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/input").click()
    time.sleep(2)

    # Kiểm tra số lượng trong giỏ hàng
    test_col_quantity = driver.find_element(By.XPATH,"/html/body/section[3]/div/table[1]/tbody[2]/tr/td[8]/input").get_attribute("value")
    
    # Kiểm tra nếu số lượng trong giỏ hàng bằng số lượng đã thêm vào
    assert int(test_col_quantity) == quantity_currently_available 