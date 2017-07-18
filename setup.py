import os

import numpy as np
from setuptools import setup
from setuptools.extension import Extension

extensions = [Extension("fast_histogram._histogram_core",
                       [os.path.join('fast_histogram', '_histogram_core.c')],
                       include_dirs=[np.get_include()])]

setup(name='fast-histogram',
      version='0.1.dev0',
      install_requires=['numpy'],
      author='Thomas Robitaille',
      author_email='thomas.robitaille@gmail.com',
      license='BSD',
      url='https://github.com/astrofrog/fastogram',
      packages=['fast_histogram'],
      ext_modules=extensions)
