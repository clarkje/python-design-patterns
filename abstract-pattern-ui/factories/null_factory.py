from .abs_factory import AbsFactory

class NullFactory(AbsFactory): 

    @staticmethod
    def create_button(): 
        raise NotImplementedError

    @staticmethod
    def create_checkbox():
        raise NotImplementedError

    @staticmethod
    def create_text_input():
        raise NotImplementedError