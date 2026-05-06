from .input import collect_input
from .math import sum
from .file import input_to_file
from .list_proce import unique
from . import input 
from . import list_proce   
from . import file
from . import math

__all__ = [
    "collect_input",
    "sum",
    "input_to_file",
    "unique"
]

__version__ = '0.4.0'

def version()->str:
    return __version__

def get_help()->None:
    print("plase read GITBUH's foxange-org user 's 'PyPI-foxange'")
    return 


if __name__ == "__main__":
    print("this is a Python 's other mod,if you want use there,plasece use 'import foxange'or 'from foxange import ...'")
    print("down is test the other mod 's text:")
    
    from os import system
    
    print("input.py:")
    system("python input.py")