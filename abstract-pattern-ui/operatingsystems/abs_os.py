import abc

class AbsOS(abc.ABC): 

    @staticmethod
    @abc.abstractmethod
    def create_button(self): 
        pass

    @staticmethod
    @abc.abstractmethod
    def create_checkbox(self): 
        pass

    @staticmethod
    @abc.abstractmethod
    def create_text_input(self): 
        pass