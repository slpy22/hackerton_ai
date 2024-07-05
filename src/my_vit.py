import requests

headers = {"Authorization": "Bearer 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"}


def vit_old_new(img_binary):
    API_URL = "https://api-inference.huggingface.co/models/Kang-Seong-Jun/oldnew_basic"
    response = requests.post(API_URL, headers=headers, data=img_binary)
    return response.json()


def vit_best_worst(img_binary):
    API_URL = "https://api-inference.huggingface.co/models/Kang-Seong-Jun/bestworst_basic"
    response = requests.post(API_URL, headers=headers, data=img_binary)
    return response.json()
