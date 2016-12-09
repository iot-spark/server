import sys
import logging
import logging.handlers

from logging import StreamHandler


class SLogger(object):
    path = "/tmp/{0}.log"
    formatter = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    def __init__(self, file_name, level=logging.INFO):
        self.file_name = file_name
        self.level = level

    def set(self):
        """
        Init logging
        :return: None
        """
        log = logging.getLogger()
        log.setLevel(self.level)
        formatter = logging.Formatter(self.formatter)

        stdout = StreamHandler(sys.stdout)
        stdout.setLevel(self.level)

        handler = logging.FileHandler(self.log_path)
        handler.setLevel(self.level)

        handler.setFormatter(formatter)

        log.addHandler(stdout)
        log.addHandler(handler)

    @property
    def log_path(self):
        return self.path.format(self.file_name)
