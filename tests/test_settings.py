import os
import unittest

from unittest import mock
from unittest.mock import MagicMock

from app.settings import Settings


class TestSettings(unittest.TestCase):
    """Unit tests for Settings class."""

    # region setup

    def setUp(self) -> None:
        """Setup before each test."""

        self._root_path = '/home/user/udaemon'

    # endregion

    # region constructor

    @mock.patch('app.settings.CustomLogger')
    def test_settings_root_path_should_be_set(
        self,
        mock_custom_logger: MagicMock
    ):
        """Root path should be set."""

        settings = Settings(self._root_path)

        expected = self._root_path
        actual = settings.ROOT_PATH

        self.assertEqual(expected, actual)

    @mock.patch('app.settings.CustomLogger')
    def test_settings_data_path_should_be_relative_to_root_path(
        self,
        mock_custom_logger: MagicMock
    ):
        """Data path should be relative."""

        settings = Settings(self._root_path)

        expected = os.path.join(self._root_path, 'data')
        actual = settings.DATA_PATH

        self.assertEqual(expected, actual)

    # endregion
