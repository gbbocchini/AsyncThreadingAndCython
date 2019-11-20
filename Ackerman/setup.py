from distutils.core import setup
from Cython.Build import cythonize
import multiprocessing

setup(
    ext_modules=cythonize("ackerman.pyx", nthreads=200)
)