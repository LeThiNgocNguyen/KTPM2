from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Điền thông tin vào form
driver.find_element(By.ID, "firstName").send_keys("Nguyen")
driver.find_element(By.ID, "lastName").send_keys("Van A")
driver.find_element(By.ID, "userEmail").send_keys("test123@email.com")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.ID, "userNumber").send_keys("0123456789")

# Chọn ngày sinh
driver.find_element(By.ID, "dateOfBirthInput").click()
driver.find_element(By.XPATH, "//option[text()='2000']").click()
driver.find_element(By.XPATH, "//option[text()='January']").click()
driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='1']").click()

# Nhập môn học
subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("Maths")
subject.send_keys(Keys.RETURN)

# Chọn sở thích
driver.find_element(By.XPATH, "//label[text()='Sports']").click()

# Nhập địa chỉ
driver.find_element(By.ID, "currentAddress").send_keys("123 Đường ABC, TP.HCM")

# Chọn State & City
state_input = driver.find_element(By.ID, "react-select-3-input")
state_input.send_keys("NCR")
state_input.send_keys(Keys.RETURN)

city_input = driver.find_element(By.ID, "react-select-4-input")
city_input.send_keys("Delhi")
city_input.send_keys(Keys.RETURN)

# Click Submit
driver.find_element(By.ID, "submit").click()

# Kiểm tra xem form có submit thành công không
try:
    modal = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
    if "Thanks for submitting the form" in modal.text:
        print("✅ Test Case Passed: Form đã được submit thành công!")
    else:
        print("❌ Test Case Failed: Form không gửi thành công.")
except:
    print("❌ Test Case Failed: Không tìm thấy thông báo xác nhận.")

# Đóng trình duyệt
time.sleep(3)
driver.quit()
