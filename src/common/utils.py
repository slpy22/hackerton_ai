import os
import joblib


class Utils:
    @staticmethod
    def get_arguments(*args):
        """
        kargs에서 args의 키들에 해 당한 값들을 꺼내서 튜플로 리턴
        :param args: 키 리스트, 마지막 값은 kargs
        :return: 밸류들 튜플
        """
        len_1 = len(args) - 1
        kargs = args[len_1]
        args = args[:len_1]
        values = []
        for key in args:
            try:
                values.append(kargs[key])
            except Exception as e:
                values.append(None)

        return tuple(values)

    @staticmethod
    def get_percentage(real, target):
        """
        실제 값이 타깃 값으로부터 몇 퍼센트 차이나는지 계산
        :param real: 실제 값
        :param target: 타깃 값
        :return: 오차 퍼센트
        """
        percent = 0
        if target == 0:
            if real - target == 0:
                percent = 0
            else:
                percent = 100
        else:
            percent = abs(real - target) * 100 / target

        percent = round(percent, 2)
        return percent

    @staticmethod
    def load_model(full_path):
        """
        모델 파일을 로드 한다.
        :param full_path: 로드 할 모델 파일 까지 풀 경로
        :return: 로드한 모델 데이터
        """
        if not os.path.isfile(full_path):
            return None
        model = joblib.load(full_path)
        return model

    @staticmethod
    def save_model(model, full_path):
        """
        모델 파일을 보존한다.
        :param model: 보존한 모델
        :param full_path: 보존 할 파일 까지의 풀 패스
        :return: 없음.
        """
        path = os.path.dirname(full_path)
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)

        joblib.dump(model, full_path)

    @staticmethod
    def delete_model(full_path):
        """
        경로내의 모델 파일 찾아서 삭제처리 한다.
        :param full_path: 삭제 할 파일까지의 풀 패스
        :return: 삭제 처리 성공 여부
        """
        if not os.path.isfile(full_path):
            return False

        os.remove(full_path)
        return True
