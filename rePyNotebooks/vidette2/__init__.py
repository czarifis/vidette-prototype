"""ignore magic"""
__version__ = '0.0.1'
from .vidette import Vidette


def load_ipython_extension(ipython):
    vidette = Vidette(ipython, 'data')
    ipython.register_magics(vidette)