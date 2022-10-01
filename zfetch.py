import os
import sys

if os.name == 'nt':
    def id(): return "windows"
else:
    from distro import id

import platform
import typing
from time import time

import psutil

from ui import DistroIcons
import ui


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
    sys_obj: platform.uname_result
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

    @property 
    def cpu_cores(self, *a, logical=True):
        return psutil.cpu_count(logical)

    @property
    def boot_time(self):
        return psutil.boot_time()

    @property
    def cpu_frequency(self):
        return (time(), self.cpu_freq.current)

    @property
    def ram_size(self):
        return self.svmem.total

    @property
    def ram_status(self):
        return (self.svmem.avaible, self.svmem.used)

    @property
    def ram_percentage(self):
        return self.svmem.percentage

    @property
    def distro_sym(self):
        var = []
        cls = DistroIcons().__class__
        for v in cls.__dict__:
            if not callable(getattr(cls, v)) and not v.startswith("__"):
                var.append(v)

        for distro in var:
            if distro.lower() in id():
                return getattr(cls, distro)
            if distro in id():
                return getattr(cls, distro)
        return DistroIcons.linux

if __name__ == "__main__":
    cpu = str(ZFetch().cpu_name) + " (" + str(ZFetch().cpu_cores) + ") " + get_human_readable_freq_size(ZFetch().cpu_frequency[0])
    ram_size = get_human_readable_memory_size(ZFetch().ram_size)
    distro = id()
    if distro != "windows":
        gpu = os.popen("lspci -vnn | grep Graphic | grep Subsystem").read().replace("Subsystem:", "").strip()
    else:
        gpu = "Unknown"

    if distro != "windows":
        wm = os.popen("echo $XDG_CURRENT_DESKTOP").read().strip()
    else:
        wm = "dWm"





