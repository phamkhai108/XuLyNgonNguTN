#file dùng để lấy dữ liệu từ web và dịch về tiếng anh xong đó đưa vào file txt

import requests
import re
from bs4 import BeautifulSoup
import langid
from googletrans import Translator
import nltk

stop_words = nltk.corpus.stopwords.words("english")
#hàm lấy dữ liệu từ web về và dịch rồi đưa về tiếng anh lưu vào file txt 
def web_data():
# URL của trang web
    url = input("Nhập vào url trang web: ")

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

        # Hàm loại bỏ kí tự đặc biệt và giữ lại dấu câu
        def remove_special_characters(text):
            cleaned_text = re.sub(r'[^\w\s.,?!]', '', text)
            return cleaned_text

        # Lấy văn bản từ các thẻ <p> và loại bỏ các đoạn trống
        text = '\n'.join([remove_special_characters(paragraph.get_text()).strip() for paragraph in paragraphs])

        # Phân tách câu bởi dấu . để xác định ngôn ngữ
        sentences = text.split(". ")

        # Xác định ngôn ngữ và dịch
        word = []
        translator = Translator()

        for sentence in sentences:
            language, score = langid.classify(sentence)

            # In kết quả
            print(sentence, '-', language, score)
            translation = translator.translate(sentence, src=language, dest='en').text
            # for w in translation.split():
            #     if w not in stop_words:
            #         translation.append(w)
            word.append(translation)


        # Lưu nội dung đã dịch vào file "A.txt"
        with open("BTL\A.txt", "a", encoding="utf-8") as file:
            for translated_sentence in word:
                file.write(translated_sentence + '\n')

        print("Nội dung đã được lưu vào file A.txt.")
    else:
        print(f"Không thể tải nội dung. Mã trạng thái: {response.status_code}")
#goi ham lay du lieu tu web

web_data()
