from .singleton import Singleton


class Config(metaclass=Singleton):
    log_file_path = './log/safety_ai'
