#!/usr/bin/env python
import sys
import subprocess

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
shellcmd('curl -O {0}'.format(venv_url))

# Untar
shellcmd('tar xzf {0}'.format(tgz_file))

# Create the initial env
shellcmd('{0} {1}/virtualenv.py {2}'.format(PYTHON, dirname, INITIAL_ENV))

# Install the virtualenv package itself into the initial env
shellcmd('{0}/bin/pip install {1}'.format(INITIAL_ENV, tgz_file))

# Cleanup
shellcmd('rm -rf {0} {1}'.format(dirname, tgz_file))
