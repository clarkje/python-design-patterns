import traceback
from factories.windows_factory import WindowsFactory
from factories.mac_factory import MacFactory
from factories.linux_factory import LinuxFactory
from factories.null_factory import NullFactory

for factory in MacFactory, WindowsFactory, LinuxFactory, NullFactory:
    f = factory()
    print(f"===== {f.__class__} =====")
    try: 
        button = f.create_button()
        button.render()
    except NotImplementedError as error: 
        if not isinstance(f,NullFactory):
            traceback.print_exc()
        else: 
            print("[Null Button] Threw Successfully")

    try: 
        checkbox = f.create_checkbox()
        checkbox.render()
    except NotImplementedError as error: 
        if not isinstance(f,NullFactory):
            traceback.print_exc()
        else: 
            print("[Null Checkbox] Threw Successfully")

    try: 
        text_input = f.create_text_input()
        text_input.render()
    except NotImplementedError as error: 
        if not isinstance(f,NullFactory):
            traceback.print_exc()
        else: 
            print("[Null TextInput] Threw Successfully")