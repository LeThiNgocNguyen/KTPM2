from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Nhập thông tin bằng XPath
driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Nguyen")
driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Van A")
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("test123@email.com")

# Chọn giới tính (Male)
driver.find_element(By.XPATH, "//label[text()='Male']").click()

# Nhập số điện thoại
driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys("0123456789")

# Chọn ngày sinh
driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']").click()
driver.find_element(By.XPATH, "//option[text()='2000']").click()
driver.find_element(By.XPATH, "//option[text()='January']").click()
driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='1']").click()

# Nhập môn học
subject = driver.find_element(By.XPATH, "//input[@id='subjectsInput']")
subject.send_keys("Maths")
subject.send_keys(Keys.RETURN)

# Chọn sở thích
driver.find_element(By.XPATH, "//label[text()='Sports']").click()

# Nhập địa chỉ
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("123 Đường ABC, TP.HCM")

# Chọn State & City
state_input = driver.find_element(By.XPATH, "//div[@id='state']//input")
state_input.send_keys("NCR")
state_input.send_keys(Keys.RETURN)

city_input = driver.find_element(By.XPATH, "//div[@id='city']//input")
city_input.send_keys("Delhi")
city_input.send_keys(Keys.RETURN)

# Click Submit
driver.find_element(By.XPATH, "//button[@id='submit']").click()

# Kiểm tra xác nhận submit thành công
time.sleep(2)  # Chờ modal hiển thị
modal = driver.find_element(By.XPATH, "//div[contains(@class,'modal-content')]")
if "Thanks for submitting the form" in modal.text:
    print("✅ Form đã được submit thành công!")
else:
    print("❌ BUG: Form không gửi thành công.")

# Đóng trình duyệt
time.sleep(3)
driver.quit()
