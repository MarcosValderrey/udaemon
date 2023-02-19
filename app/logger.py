import logging
import os


class CustomLogger():
    """
    Override behavior for default Python logger.
    """

    def __init__(
        self,
        root_path: str,
        datetime_format: str,
        log_format: str
    ) -> None:
        """
        Constructor.
        
        Parameters
        ----------
        root_path : str
            Root project path.
        datetime_format : str
            Datetime format for logging.
        log_format : str
            Format for every log message.
        """

        # Basic log formatter (to share across console and file loggers)
        log_formatter = logging.Formatter(
            fmt=log_format,
            datefmt=datetime_format
        )

        # Root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)

        # Console logger
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(log_formatter)
        root_logger.addHandler(console_handler)

        # File logger
        logs_folder = os.path.join(root_path, 'data')
        os.makedirs(logs_folder, exist_ok=True)

        logs_path = os.path.join(logs_folder, 'udaemon.log')
        file_handler = logging.FileHandler(logs_path)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(log_formatter)
        root_logger.addHandler(file_handler)
