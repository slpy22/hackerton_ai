import os
from pathlib import Path
import base64
from flask import jsonify
from mimetypes import guess_type
from my_langchain import extract_information, recommend_estate


# Function to encode a local image into data URL
def image_to_data_url(image_file):
    mime_type, _ = guess_type(image_file.filename)
    # Default to png
    if mime_type is None:
        mime_type = 'image/png'

    base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Construct the data URL
    return f"data:{mime_type};base64,{base64_encoded_data}"


def predict(img_file):
    """
    이미지 분석하여 후보 추천 하는 함수
    :return: 매물 위치 도로명 주소의 배열
    """
    # file_path = os.path.join(os.getcwd(), img_file.filename)
    # img_file.save(file_path)

    img_data = image_to_data_url(img_file)

    information = extract_information(img_data)
    addresses = recommend_estate(information)
    # addresses = ["123 Main St, Springfield, IL", "456 Elm St, Shelbyville, IL"]  # 예제 응답

    # os.remove(file_path)
    return jsonify(addresses), 200
