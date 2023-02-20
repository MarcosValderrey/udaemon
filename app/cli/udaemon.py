import argparse
import logging
import os
import shutil

from app.cli.systemctl import SystemctlCLI
from app.settings import Settings


class UdaemonCLI():
    """
    Command line interface to daemonize python projects.
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
        self._systemctl = SystemctlCLI(argv, settings)
        self._udaemon_actions = [
            'add',
            'remove',
            'list'
        ]
        self._systemctl_actions = [
            'enable',
            'disable',
            'start',
            'stop',
            'status'
        ]
        self._all_actions = self._udaemon_actions + self._systemctl_actions

        self._parse_argv(argv[1:])

    def _parse_argv(self, argv: list):
        """
        Parse arguments from argv.

        Parameters
        ----------
        argv : list
            Main program parameters.
        """

        self.argv = argv
        self.parser = argparse.ArgumentParser('Udaemon')

        self.parser.add_argument(
            'action',
            type=str,
            choices=self._all_actions,
            help='internal action to run'
        )

        self.parser.add_argument(
            'service_name',
            type=str,
            nargs='?',
            help='service name'
        )

        self.parser.add_argument(
            'service_path',
            type=str,
            nargs='?',
            help='service path to add to available list'
        )

        self.args = self.parser.parse_args(self.argv)

    def add_service(self, service_name: str, service_path: str):
        """
        Add service to available list.

        Parameters
        ----------
        service_name : str
            Service name (with .service extension).
        service_path : str
            Path to service file trying to been added.
        """

        service_src_path = os.path.abspath(service_path)
        user_services = self._settings.SYSTEMD_USER_SERVICES
        service_dst_path = os.path.join(user_services, service_name)

        logging.debug('adding service %s from %s', service_name, service_src_path)

        os.makedirs(user_services, exist_ok=True)

        if (os.path.exists(service_dst_path)):
            logging.info('service %s already exists to deploy', service_name)
        else:
            shutil.copyfile(service_src_path, service_dst_path)
            logging.info('service %s added for user', service_name)

            self._systemctl.action('enable', service_name)
            self._systemctl.action('start', service_name)

    def remove_service(self, service_name: str) -> int:
        """
        Remove service from available list.

        Parameters
        ----------
        service_name : str
            Service name (with .service extension).
        """

        user_services = self._settings.SYSTEMD_USER_SERVICES
        service_path = os.path.join(user_services, service_name)

        logging.debug('removing service %s from %s', service_name, user_services)

        if (os.path.exists(service_path)):
            self._systemctl.action('stop', service_name)
            self._systemctl.action('disable', service_name)

            os.remove(service_path)
            logging.info('service %s has been removed', service_name)
            return 0
        else:
            logging.error('no service %s to remove', service_name)
            return 1

    def list_available(self) -> int:
        """
        List available services to daemonize.
        """

        folder = self._settings.SYSTEMD_USER_SERVICES
        services = []

        for filename in os.listdir(folder):
            if (filename.endswith('.service') == False):
                continue

            services.append(filename)

        if (len(services) > 0):
            logging.info('available services: %s', services)
        else:
            logging.info('no services deployed yet')

        return 0

    def run(self) -> int:
        """
        Run program with the specified parameters.
        """

        action = self.args.action
        service_name = self.args.service_name
        service_path = self.args.service_path

        if (service_name and service_name.endswith('.service') == False):
            service_name = '{}.service'.format(service_name)

        if (action in self._udaemon_actions):
            if (action == 'list'):
                return self.list_available()
            if (action == 'add'):
                return self.add_service(service_name, service_path)
            elif (action == 'remove'):
                return self.remove_service(service_name)
        elif (action in self._systemctl_actions):
            return self._systemctl.action(action, service_name)
