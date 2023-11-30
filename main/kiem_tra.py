import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
import re
import nltk

# URL của trang web
url = "https://vnexpress.net/"

# Sử dụng requests để tải nội dung trang web
response = requests.get(url)

# Kiểm tra xem việc tải nội dung thành công hay không
if response.status_code == 200:
    # Lấy nội dung HTML của trang web
    html = response.text

    # Tạo một đối tượng BeautifulSoup để phân tích nội dung HTML
    soup = BeautifulSoup(html, "html.parser")

    # Tìm tất cả các thẻ <p> và lấy nội dung từ chúng
    paragraphs = soup.find_all('p')

    # Hàm để chỉ loại bỏ kí tự đặc biệt và xóa dấu tiếng Việt
    def clean_text(text):
        cleaned_text = re.sub(r'[^\w\s.,?!]', '', unidecode(text))
        return cleaned_text.strip()

    # Lấy văn bản từ các thẻ <p>, loại bỏ kí tự đặc biệt, và xóa dấu tiếng Việt
    text = '\n'.join([clean_text(paragraph.get_text()) for paragraph in paragraphs])


    # Lưu nội dung vào file
    with open("doan_10.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("Nội dung đã được lưu vào file doan_10.txt.")
else:
    print(f"Không thể tải nội dung. Mã trạng thái: {response.status_code}")
