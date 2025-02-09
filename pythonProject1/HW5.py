import colorama
import inspect
import sys

print(colorama.__name__)

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))

for modul_name, modul_path in sys.modules.items():
    print(modul_name, modul_path)

