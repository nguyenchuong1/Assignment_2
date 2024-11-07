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
def test_View_product_details_by_main_menu(driver): 
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[4]/div/div/div[2]/div[2]/div[2]/a/input").click()  # chọn thực đơn trên main menu
    time.sleep(1)
    assert "http://localhost/B08/index.php?quanly=dt&id=TS2" in driver.current_url

def test_View_product_details_in_homepage(driver): 
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.XPATH,"/html/body/section[3]/div/div[2]/div/div[1]/div[2]/a/input").click()
    assert "http://localhost/B08/index.php?quanly=dt&id=TS1" in driver.current_url


def test_View_product_details_by_search(driver): 
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.CLASS_NAME, "menu-bar").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[1]").send_keys("Caramel")  # search name item
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[1]/header/div/div/div[3]/ul/li[1]/form/input[2]").click()
    time.sleep(1)
    name=driver.find_element(By.XPATH,"/html/body/section[3]/div/div/div/div/div[2]/div[1]").text
    driver.find_element(By.XPATH, "/html/body/section[3]/div/div/div/div/div[2]/a/input").click()  # chọn thực đơn trên main menu
    time.sleep(1)
    assert "Trà sữa Caramel" in name

def test_View_product_details_by_menu_in_homepage(driver): 
    driver.get("http://localhost/B08/index.php")
    driver.find_element(By.XPATH, "/html/body/section[2]/div/button/a").click()  # chọn menu trên ảnh home page
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/section[4]/div/div/div[2]/div[1]/div[2]/a/input").click()
    assert "http://localhost/B08/index.php?quanly=dt&id=TS1" in driver.current_url