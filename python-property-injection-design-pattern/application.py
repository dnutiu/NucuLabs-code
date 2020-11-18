from input_listener import InputListener, ConsoleInputListener
from message import Message
from printer import Printer, ConsolePrinter, Rot13Encoder
from translator import Translator, RomanianTranslator


class MessageTranslator:
    def __init__(self, translator: Translator, printer: Printer):
        if not translator:
            raise ValueError("Translator cannot be None.")
        if not printer:
            raise ValueError("Printer cannot be None.")

        self._translator = translator
        self._printer = printer

    def translate(self, message):
        return self._translator.translate(message)

    def print(self, message):
        self._printer.print(message)


class Application:
    def __init__(self):
        self._input_listener: InputListener = ConsoleInputListener("< ")

    def start(self):
        print("starting application.")
        console_printer = ConsolePrinter(">")
        console_printer.encoder = Rot13Encoder()
        message_translator = MessageTranslator(RomanianTranslator(), console_printer)
        while True:
            user_in = Message(self._input_listener.get_input())
            if str(user_in) == "exit":
                exit(0)

            translated_message = message_translator.translate(user_in)
            message_translator.print(translated_message)
