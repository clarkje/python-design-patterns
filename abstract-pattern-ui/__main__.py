from factories.windows_factory import WindowsFactory
from factories.mac_factory import MacFactory
from factories.linux_factory import LinuxFactory

for factory in MacFactory, WindowsFactory, LinuxFactory:
    f = factory()
    f.create_button()
    f.create_checkbox()
    f.create_textInput()
