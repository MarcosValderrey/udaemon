import os
import sys

from app.cli.udaemon import UdaemonCLI
from app.settings import Settings


if (__name__ == '__main__'):
    root_path = os.path.abspath(os.path.dirname(__file__))
    settings = Settings(root_path)

    UdaemonCLI(sys.argv, settings).run()
