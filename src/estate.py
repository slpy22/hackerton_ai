import gc
import time
import numpy as np
import pandas as pd
from ..common.log_config import log

def predict(img_file):
    """
    이미지 분석하여 후보 추천 하는 함수
    :return: 매물 위치 도로명 주소의 배열
    """
    ret = [(0 if sdid not in limit_table.keys() or item < limit_table[sdid] else 1) for item in ret]
    ret = str(ret)
    return ret, 200
