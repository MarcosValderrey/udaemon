import logging
import subprocess

from app.settings import Settings


class SystemctlCLI():
    """
    Command line interface wrapper around systemctl.
    """

    def __init__(self, argv: list, settings: Settings):
        """
        Constructor.

        Parameters
        ----------
        argv : list
            Main program parameters.
        settings : app.settings.Settings
            Udaemon specific settings.
        """

        self._settings = settings
        self._base_command = [
            'systemctl',
            '--user'
        ]

    def action(self, action: str, service_name: str):
        """
        Run systemctl status command for service.

        Parameters
        ----------
        action : str
            Action corresponding to a given systemctl internal command.
        service_name : str
            Service name (with .service extension).
        """

        command = [
            *self._base_command,
            action,
            service_name
        ]

        self._run(command)

    def _run(self, command: list):
        """
        Run custom systemctl command.

        Parameters
        ----------
        command : list
            List of tokens to execute.
        """

        result = subprocess.run(command)

        logging.debug('systemctl: %s', result)
