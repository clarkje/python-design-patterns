import argparse
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

parser = argparse.ArgumentParser( 
    prog='abstract-pattern-ui', 
    description='educational implementation of abstract factory pattern',
)

parser.add_argument('-os','--os',type=str, help="Specify the OS to use --os=<Mac|Windows|Linux> - Unsupported options should throw a NotImplementedError")
parser.add_argument('-all','--all',action='store_true',help="Print output from all OS types, including null")
args = parser.parse_args()

if args.os is not None: 
    match args.os.lower():
        case "windows": 
            render_ui(WindowsFactory())
        case "mac": 
            render_ui(MacFactory())
        case "linux": 
            render_ui(LinuxFactory())
        case _:
            render_ui(NullFactory())
elif args.all: 
    for factory_class in [MacFactory, WindowsFactory, LinuxFactory, NullFactory]: 
        render_ui(factory_class())