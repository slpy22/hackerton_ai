import os
from pathlib import Path
import base64
from flask import jsonify
from mimetypes import guess_type
from my_langchain import extract_information, recommend_estate
from my_vit import vit_old_new, vit_best_worst


# Function to encode a local image into data URL
def image_to_data_url(image_file):
    mime_type, _ = guess_type(image_file.filename)
    # Default to png
    if mime_type is None:
        mime_type = 'image/png'

    base64_encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Construct the data URL
    return f"data:{mime_type};base64,{base64_encoded_data}"


def by_gpt(img_file):
    """
    이미지 분석하여 해당 지역 부동산 관련 정보 추출
    :return: 부동산정보 설명
    """
    img_data = image_to_data_url(img_file)
    information = extract_information(img_data)
    # addresses = recommend_estate(information)
    return jsonify(information), 200


def by_vit(img_file):
    """
    이미지 분석하여 해당 지역 부동산 관련 정보 추출
    :return: 부동산정보 설명
    """
    img_binary = img_file.read()
    result = vit_best_worst(img_binary)
    result.extend(vit_old_new(img_binary))
    return result
