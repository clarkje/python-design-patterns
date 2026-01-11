from computer_director import ComputerDirector
from computer_builder import ComputerBuilder

director = ComputerDirector()
gaming_pc = director.build_gaming_pc()
gaming_pc = director.build_gaming_pc()
print(f"Gaming PC:\n{gaming_pc.__repr__()}\n")