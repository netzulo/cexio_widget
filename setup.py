from setuptools import setup, find_packages
from os import path
from os import name

CURR_PATH = path.abspath(path.dirname(__file__))

setup(name='cexio_widget',
      version='0.0.0',
      packages=find_packages(exclude=['tests']),
      description = 'CEX.IO widget GUI for handle exchange account from installed APP. lin/win Edit',
      author = 'Netzulo Open Source',
      author_email = 'netzuleando@gmail.com',
      url = 'https://github.com/netzulo/cexio_widget',
      download_url = 'https://github.com/netzulo/cexio_widget/tarball/v0.0.1',
      keywords = ['cexio','trading','bitcoin','exchange', 'crypto', 'bot'],
      install_requires=['wxPython==4.0.0b1']
      )
