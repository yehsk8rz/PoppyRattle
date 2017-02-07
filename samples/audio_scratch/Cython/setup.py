from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("hello.pyx",souces=["hello.cpp"],language="c++") + cythonize("fib.pyx",souces=["fib.cpp"],language="c++"))


