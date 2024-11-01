import abc
class MedicalParser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text
    @abc.abstractmethod
    def parser(self):
        pass