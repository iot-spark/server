from abc import ABCMeta, abstractmethod


class Base(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass
