from __future__ import print_function
from time import time
import typing

import ui
import psutil

import platform

class ZFetch:
    sys_obj: platform.uname_result
    cpu_freq: typing.Any
    
    def __init__(self):
        self.sys_obj = platform.uname()
        self.cpu_freq = psutil.cpu_freq()

    @property
    def __system_obj__(self) -> platform.uname_result:
        return self.sys_obj
    
    @property
    def cpu_name(self):
        return platform.processor()

    def cpu_cores(self, *a, logical=True):
        return psutil.cpu_count(logical)
    
    @property
    def boot_time(self):
        return psutil.boot_time()
    
    @property
    def get_cpu_freq(self):
        return (time(), self.cpu_freq.current)