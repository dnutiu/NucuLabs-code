import abc

from message import Message


class Printer(metaclass=abc.ABCMeta):
    def print(self, message):
        raise NotImplementedError("print is not implemented")


class ConsolePrinter(Printer):
    def __init__(self, prefix: str):
        self._prefix = prefix

    def print(self, message: Message):
        print(self._prefix, message)


class VoidPrinter(Printer):
    def print(self, message):
        pass
