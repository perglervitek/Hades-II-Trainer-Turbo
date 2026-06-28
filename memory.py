import pymem
import pymem.process
import ctypes
from ctypes import wintypes

class EliteMemory:
    def __init__(self):
        self.pm = None
        self.process_handle = None
        self.base_address = 0

    def connect(self, process_name="Hades2.exe"):
        self.pm = pymem.Pymem(process_name)
        self.process_handle = self.pm.process_handle
        module = pymem.process.module_from_name(self.pm.process_handle, "Hades2.exe")
        if not module:
            raise Exception("Game module not found")
        self.base_address = module.lpBaseOfDll

    def read_int(self, address):
        return self.pm.read_int(address)

    def write_int(self, address, value):
        self.pm.write_int(address, value)

    def read_float(self, address):
        return self.pm.read_float(address)

    def write_float(self, address, value):
        self.pm.write_float(address, value)

    def read_bytes(self, address, length):
        return self.pm.read_bytes(address, length)

    def write_bytes(self, address, data):
        self.pm.write_bytes(address, data, len(data))

    def follow_pointer(self, base, offsets):
        addr = self.pm.read_int(base)
        for offset in offsets[:-1]:
            if addr == 0:
                return 0
            addr = self.pm.read_int(addr + offset)
        return addr + offsets[-1] if addr != 0 else 0
