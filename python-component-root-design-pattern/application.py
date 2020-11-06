from input_listener import InputListener, ConsoleInputListener
from message import Message
from printer import Printer, ConsolePrinter
from translator import Translator, RomanianTranslator


class Application:
    def __init__(self):
        self._printer: Printer = ConsolePrinter(">")
        self._translator: Translator = RomanianTranslator()
        self._input_listener: InputListener = ConsoleInputListener("< ")

    def start(self):
        print("starting application.")
        while True:
            user_in = Message(self._input_listener.get_input())
            if str(user_in) == "exit":
                exit(0)

            self._printer.print(self._translator.translate(user_in))
