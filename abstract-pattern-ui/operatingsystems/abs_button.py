import abc

class AbsButton(abc.ABC): 

    @staticmethod
    @abc.abstractmethod
    def render():
        pass