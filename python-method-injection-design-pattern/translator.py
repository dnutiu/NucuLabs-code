import abc

from message import Message


class Translator(metaclass=abc.ABCMeta):
    def translate(self, message: Message) -> Message:
        raise NotImplementedError("translate must be implemented!")


class RomanianTranslator(Translator):
    def translate(self, message: Message) -> Message:
        words_map = {"hello": "salut"}
        message_words = str(message).split(" ")

        for index, word in enumerate(message_words):
            if word.lower() in words_map.keys():
                message_words[index] = words_map[word.lower()]

        return Message(" ".join(message_words))
