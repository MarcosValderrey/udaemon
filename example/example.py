import logging
import os
import signal
import time


class GracefulKiller():
    """
    Helper to exit program gracefully.
    """

    def __init__(self) -> None:
        """Constructor."""

        self.running = True

        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        """
        Exit program gracefully.
        """

        self.running = False


def configure_logging():
    """
    Configure basic logging to test service.
    """

    _DATETIME_FORMAT = '%Y-%m-%d %I:%M:%S'
    _LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'

    # Basic log formatter (to share across console and file loggers)
    log_formatter = logging.Formatter(
        fmt=_LOG_FORMAT,
        datefmt=_DATETIME_FORMAT
    )

    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Console logger
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    # console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    # File logger
    logs_path = os.path.abspath(os.path.dirname(__file__))
    logs_path = os.path.join(logs_path, 'example.log')

    file_handler = logging.FileHandler(logs_path)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)


def example_service():
    """
    Example test loop.
    """

    logging.info('example start')
    killer = GracefulKiller()

    while killer.running:
        logging.info('heartbeat')
        time.sleep(10)

    logging.info('example end')


if (__name__ == '__main__'):
    configure_logging()
    example_service()
