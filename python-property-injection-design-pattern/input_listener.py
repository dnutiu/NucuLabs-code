import abc


class InputListener(metaclass=abc.ABCMeta):
    def get_input(self) -> str:
        raise NotImplementedError("get_input is not implemented!")


class ConsoleInputListener(InputListener):
    def __init__(self, prompt: str):
        self._prompt = prompt

    def get_input(self) -> str:
        return input(self._prompt)
