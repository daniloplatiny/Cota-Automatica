import sys
from cx_Freeze import setup, Executable
import json
import tkinter
import utm
import principal
import entradas
import openUrl
import datum1ToDatum2

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["json, utm,tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "Cota Automatica",
      version = "1",
      author = 'Danilo Platiny',
      author_email = 'danilo.platiny@gmail.com',
      description = "Cota Automatica",
      options = {"build_exe": build_exe_options},
      executables = [Executable("CotaAutomatica.py")]
      )
