import abc
import codecs
from message import Message


class Encoder(metaclass=abc.ABCMeta):
    def encode(self, message: Message) -> Message:
        raise NotImplementedError("encode must be implemented!")


class Printer(metaclass=abc.ABCMeta):
    def print(self, message: Message, encoder: Encoder):
        raise NotImplementedError("print is not implemented")


class Rot13Encoder(metaclass=abc.ABCMeta):
    def encode(self, message: Message) -> Message:
        return Message(codecs.encode(str(message), 'rot_13'))


class NullEncoder(metaclass=abc.ABCMeta):
    def encode(self, message: Message) -> Message:
        return message


class ConsolePrinter(Printer):
    def __init__(self, prefix: str):
        self._prefix = prefix

    def print(self, message: Message, encoder: Encoder):
        print(self._prefix, encoder.encode(message))


class VoidPrinter(Printer):
    def print(self, message, encoder: Encoder):
        pass
