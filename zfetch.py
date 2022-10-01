from __future__ import print_function

import ui
import psutil

import platform

class ZFetch:
    sys_obj: platform.uname_result
    
    def __init__(self):
        self.sys_obj = platform.uname()

    @property
    def __system_obj__(self) -> platform.uname_result:
        return self.sys_obj
    
    @property
    def cpu_name():
        return platform.processor()


    def cpu_cores(*a, logical=True):
        return psutil.cpu_count(logical)