import logging
import os

from app.logger import CustomLogger


class Settings():
    """
    Settings collection for Udaemon.
    """

    def __init__(self, root_path: str) -> None:
        """
        Constructor.
        
        Parameters
        ----------
        root_path : str
            Root project path.
        """

        # Folders
        self.ROOT_PATH = root_path
        self.DATA_PATH = os.path.join(root_path, 'data')
        self.USER_HOME = os.path.expanduser('~')
        self.SYSTEMD_ROOT_SERVICES = os.path.normpath('/etc/systemd/system')
        self.SYSTEMD_USER_SERVICES = os.path.join(self.USER_HOME, '.config/systemd/user')

        # Formats
        self.DATETIME_FORMAT = '%Y-%m-%d %I:%M:%S'
        self.LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'

        self.logger = CustomLogger(root_path, self.DATETIME_FORMAT, self.LOG_FORMAT)

        # logging.debug('SYSTEMD_ROOT_SERVICES = %s', self.SYSTEMD_ROOT_SERVICES)
        # logging.debug('SYSTEMD_USER_SERVICES = %s', self.SYSTEMD_USER_SERVICES)
