import sys

from cx_Freeze import setup, Executable



setup(  name = "instaCrol",
        version = "1.0",
        description = "ericH All right",
        author = "ericH",
        executables = [Executable("instagram.py")]) 

