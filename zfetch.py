from __future__ import print_function
from time import time
import typing

import ui
import psutil

import platform

from ui import DistroIcons

def get_human_readable_freq_size(bytes, suffix="Hz"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MHz'
        1253656678 => '1.17GHz'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def get_human_readable_memory_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

class ZFetch:
    sys_obj: typing.Any
    cpu_freq: typing.Any
    svmem: typing.Any
    
    def __init__(self):
        self.sys_obj = platform.uname()
        self.cpu_freq = psutil.cpu_freq()
        self.svmem = psutil.virtual_memory()
        
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
    
    @property
    def get_ram_size(self):
        return self.svmem.total
    
    @property
    def get_ram_status(self):
        return (self.svmem.avaible, self.svmem.used)
    
    @property
    def get_ram_percentage(self):
        return self.svmem.percentage