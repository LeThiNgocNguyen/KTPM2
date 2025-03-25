import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://example-ecommerce.com")
    driver.maximize_window()
    yield driver
    driver.quit()

# Test Case 1: Đăng nhập hợp lệ
def test_valid_login(setup):
    driver = setup
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
    driver.find_element(By.NAME, "email").send_keys("test@example.com")
    driver.find_element(By.NAME, "password").send_keys("Password123" + Keys.RETURN)
    
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url

# Test Case 2: Thêm sản phẩm vào giỏ hàng
def test_add_to_cart(setup):
    driver = setup
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "product-1"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cart"))).click()
    
    cart_items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart-item")))
    assert len(cart_items) > 0

# Test Case 3: Đăng xuất
def test_logout(setup):
    driver = setup
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("test@example.com")
    driver.find_element(By.NAME, "password").send_keys("Password123" + Keys.RETURN)
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout-button"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-button")))
    assert "login" in driver.current_url

# Test Case 4: Kiểm tra tổng giá trị đơn hàng
def test_check_cart_total(setup):
    driver = setup
    driver.find_element(By.ID, "product-1").click()
    driver.find_element(By.ID, "add-to-cart").click()
    driver.find_element(By.ID, "product-2").click()
    driver.find_element(By.ID, "add-to-cart").click()
    driver.find_element(By.ID, "cart").click()
    
    total_price = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cart-total"))).text
    assert float(total_price.replace("$", "")) > 0
