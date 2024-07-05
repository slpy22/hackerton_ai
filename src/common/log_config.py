import logging.handlers
from .conf import Config


# 루트 로그 취득
log = logging.getLogger()
log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

# 콘솔의 출력 포맷 설정
if log.hasHandlers():
    log.handlers[0].setFormatter(formatter)
else:
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)

# 로그 파일에로의 출력 포맷 설정
timed_file_handler = logging.handlers.TimedRotatingFileHandler(filename=Config.log_file_path, when='midnight', interval=1,
                                                               encoding='utf-8')
timed_file_handler.setFormatter(formatter)
timed_file_handler.suffix = "%Y%m%d"
log.addHandler(timed_file_handler)
