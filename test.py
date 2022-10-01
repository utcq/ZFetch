import rich
from zfetch import ZFetch

def check_zfetch_properties(callable = rich.print):
    instance = ZFetch()
    
    for property in dir(instance):
        callable(property)


if __name__ == '__main__':
    check_zfetch_properties()