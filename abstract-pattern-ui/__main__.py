import traceback
from factories.windows_factory import WindowsFactory
from factories.mac_factory import MacFactory
from factories.linux_factory import LinuxFactory
from factories.null_factory import NullFactory

def render_ui(factory): 
    print(f"===== {factory.__class__} =====")

    components = [
        ("Button", factory.create_button), 
        ("Checkbox", factory.create_checkbox), 
        ("TextInput", factory.create_text_input)
    ]

    for name, create_func in components: 
        try: 
            component = create_func()
            component.render()
        except NotImplementedError: 
            if isinstance(factory, NullFactory): 
                print(f"[Null {name}] Threw Successfully")
            else: 
                raise

for factory_class in [MacFactory, WindowsFactory, LinuxFactory, NullFactory]: 
    render_ui(factory_class())