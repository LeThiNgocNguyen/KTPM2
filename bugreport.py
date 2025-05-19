from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Hàm kiểm tra số điện thoại hợp lệ (10 chữ số)
def is_valid_phone(phone_number):
    return re.fullmatch(r"\d{10}", phone_number) is not None

# Nhập thông tin không hợp lệ
driver.find_element(By.ID, "firstName").send_keys("Nguyen")
driver.find_element(By.ID, "lastName").send_keys("Van A")
driver.find_element(By.ID, "userEmail").send_keys("invalid-email")  # Email sai định dạng
driver.find_element(By.XPATH, "//label[text()='Male']").click()

# Nhập số điện thoại không hợp lệ (chỉ có 8 chữ số)
phone_input = driver.find_element(By.ID, "userNumber")
invalid_phone = "12345678"
phone_input.send_keys(invalid_phone)

# Kiểm tra nếu số điện thoại không hợp lệ nhưng vẫn cho nhập
if is_valid_phone(invalid_phone):
    print("Số điện thoại hợp lệ.")
else:
    print("BUG: Form vẫn chấp nhận số điện thoại không hợp lệ!")

# Chọn ngày sinh
driver.find_element(By.ID, "dateOfBirthInput").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[text()='1999']").click()
driver.find_element(By.XPATH, "//option[text()='December']").click()
driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='25']").click()

