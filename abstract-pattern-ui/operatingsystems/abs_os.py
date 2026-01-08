import abc

class AbsOS(abc.ABC): 

    @staticmethod
    @abc.abstractmethod
    def create_button(): 
        pass

    @staticmethod
    @abc.abstractmethod
    def create_checkbox(): 
        pass

    @staticmethod
    @abc.abstractmethod
    def create_text_input(): 
        pass