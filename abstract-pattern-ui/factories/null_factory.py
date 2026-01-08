from .abs_factory import AbsFactory

class NullFactory(AbsFactory): 

    def __init__(self): 
        print("===== NULL OS =====")
     
    @staticmethod
    def create_button(): 
        raise NotImplementedError

    @staticmethod
    def create_checkbox():
        raise NotImplementedError

    @staticmethod
    def create_textInput():
        raise NotImplementedError