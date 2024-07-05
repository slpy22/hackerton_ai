from src.sensing.data_set import Dataset
from src.sensing.data_preview import DataPreview
from src.common.log_config import log

if __name__ == "__main__":
    # dataset = Dataset()
    # last_file_time = dataset.load()
    # dataset.save(last_file_time)
    log.info('test log')
    DataPreview.load_n_preview()
