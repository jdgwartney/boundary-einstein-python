#!/usr/bin/env python
import os
import shutil
import sys
import subprocess
import tarfile
import urllib

VENV_VERSION = '1.9.1'
PYPI_VENV_BASE = 'http://pypi.python.org/packages/source/v/virtualenv'
PYTHON = 'python2'
INITIAL_ENV = 'py-env0'

def shellcmd(cmd, echo=True):
    """ Run 'cmd' in the shell and return its standard out.
    """
    if echo: print '[cmd] {0}'.format(cmd)
    out = subprocess.check_output(cmd, stderr=sys.stderr, shell=True)
    if echo: print out
    return out

dirname = 'virtualenv-' + VENV_VERSION
tgz_file = dirname + '.tar.gz'

# Fetch virtualenv from PyPI
venv_url = PYPI_VENV_BASE + '/' + tgz_file
urllib.urlretrieve(venv_url,tgz_file)

# Untar
tar = tarfile.open(tgz_file,"r:gz")
tar.extractall()

# Create the initial env
shellcmd('{0} {1}/virtualenv.py {2}'.format(PYTHON, dirname, INITIAL_ENV))

# Install the virtualenv package itself into the initial env
shellcmd('{0}/bin/pip install {1}'.format(INITIAL_ENV, tgz_file))

# Cleanup
os.remove(tgz_file)
shutil.rmtree(dirname)
