import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Image Processing Project",
    version = "1.0",
    description = "Swiss Army knife for Image Processing",
    author = "Najeh Halawani",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
