from input_listener import InputListener, ConsoleInputListener
from message import Message
from printer import Printer, ConsolePrinter, Rot13Encoder
from translator import Translator, RomanianTranslator


class MessageTranslator:
    def __init__(self, translator: Translator):
        if not translator:
            raise ValueError("Translator cannot be None.")

        self._translator = translator

    def translate(self, message):
        return self._translator.translate(message)


class Application:
    def __init__(self):
        self._input_listener: InputListener = ConsoleInputListener("< ")

    def start(self):
        print("starting application.")
        console_printer = ConsolePrinter(">")
        message_translator = MessageTranslator(RomanianTranslator())
        while True:
            user_in = Message(self._input_listener.get_input())
            if str(user_in) == "exit":
                exit(0)

            translated_message = message_translator.translate(user_in)
            console_printer.print(translated_message, Rot13Encoder())
