import os
import unittest

from unittest import mock
from unittest.mock import MagicMock

from app.logger import CustomLogger


class TestCustomLogger(unittest.TestCase):
    """Unit tests for CustomLogger class."""

    # region setup

    def setUp(self) -> None:
        """Setup before each test."""

        self._root_path = '/home/user/udaemon'
        self._DATETIME_FORMAT = '%Y-%m-%d %I:%M:%S'
        self._LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'

    # endregion

    # region constructor

    @mock.patch('app.logger.logging.FileHandler')
    @mock.patch('app.logger.os.makedirs')
    def test_logger(
        self,
        mock_os_path_makedirs: MagicMock,
        mock_logging_FileHandler: MagicMock
    ):
        """Root path should be set."""

        logger = CustomLogger(
            self._root_path,
            self._DATETIME_FORMAT,
            self._LOG_FORMAT
        )

        """
        expected = self._root_path
        actual = self.settings.ROOT_PATH

        self.assertEqual(expected, actual)
        """

    # endregion
