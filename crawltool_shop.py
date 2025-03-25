import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    """Khởi tạo trình duyệt Chrome với Selenium"""
    options = Options()
    options.add_argument("--headless")  # Chạy không hiển thị giao diện
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def crawl_shopee_products(search_keyword, max_pages=3):
    """Crawl danh sách sản phẩm trên Shopee theo từ khóa tìm kiếm"""
    driver = setup_driver()
    products = []
    
    for page in range(max_pages):
        url = f"https://shopee.vn/search?keyword={search_keyword}&page={page}"
        print(f" Đang crawl trang {page + 1}: {url}")
        driver.get(url)
        time.sleep(5)  # Chờ trang tải xong

        try:
            # Chờ các sản phẩm tải xong
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.shopee-search-item-result__item"))
            )

            # Lấy HTML của trang và phân tích với BeautifulSoup
            soup = BeautifulSoup(driver.page_source, "html.parser")
            items = soup.select("div.shopee-search-item-result__item")

            for item in items:
                try:
                    # Lấy tên sản phẩm
                    name = item.select_one(".Cve6sh").text.strip()

                    # Lấy giá sản phẩm
                    price = item.select_one(".kJjFOd").text.strip()

                    # Lấy số lượng đã bán
                    sold = item.select_one(".r6HknA")
                    sold = sold.text.strip() if sold else "Không có dữ liệu"

                    # Lấy đánh giá
                    rating = item.select_one(".shopee-rating-stars__stars")
                    rating = len(rating.find_all("div", class_="shopee-rating-stars__star-wrapper")) if rating else "Không có đánh giá"

                    # Lấy link sản phẩm
                    link_tag = item.select_one("a")
                    link = "https://shopee.vn" + link_tag["href"] if link_tag else "Không có link"

                    # Thêm vào danh sách
                    products.append({
                        "Tên sản phẩm": name,
                        "Giá": price,
                        "Số lượng đã bán": sold,
                        "Đánh giá": rating,
                        "Link": link
                    })
                except Exception as e:
                    print(f" Lỗi khi lấy dữ liệu sản phẩm: {e}")

        except Exception as e:
            print(f" Lỗi khi tải trang: {e}")

    driver.quit()

    # Lưu vào file CSV
    df = pd.DataFrame(products)
    df.to_csv("shopee_products.csv", index=False, encoding="utf-8-sig")

    print(f" Đã lưu {len(products)} sản phẩm vào file shopee_products.csv")
    return products

# 🛒 Nhập từ khóa cần tìm kiếm trên Shopee
search_keyword = "tai nghe bluetooth"
shopee_products = crawl_shopee_products(search_keyword, max_pages=3)
