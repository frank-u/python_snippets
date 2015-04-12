"""
Created on 06.12.2012

@author: Oleksandr Poliatykin
"""
import ctypes
import os

try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

print("Is admin: {0}".format(is_admin))