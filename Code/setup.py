#import sys
#from cx_Freeze import setup, Executable
#import os
#os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Python35\\tcl\\tcl8.6"

#os.environ['TK_LIBRARY'] = "C:\\Program Files\\Python35\\tcl\\tk8.6"
# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
#base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

#setup(  name = "Pythagore",
#       version = "0.1",
#        description = "Calculatrice pour Pythagore!",
#       executables = [Executable("PythagoreGUI.py", base=base)]

#   )
from setuptools import setup
import py2exe

setup(console=['PythagoreGUI.py'])