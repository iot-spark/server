from abc import ABCMeta, abstractmethod


class Base(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        pass
