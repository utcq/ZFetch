import rich
from zfetch import ZFetch

print = rich.print
instance = ZFetch()

def check_zfetch_properties():
    for property in dir(instance):
        print(property)

def run_zfetch_functions():
    for property in dir(instance):
        if not property.startswith("__"):
            if hasattr(property, '__call__'):
                print(property.__name__ + ": ")

if __name__ == '__main__':
    run_zfetch_functions()