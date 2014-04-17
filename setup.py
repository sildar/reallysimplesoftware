try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple RSS Reader that allows local copy and direct video watching.',
    'author': 'Remi [Sildar] Bois',
    'url': 'https://github.com/sildar/reallysimplesoftware',
    'download_url': 'https://github.com/sildar/reallysimplesoftware.git',
    'author_email': 'sildar44@gmail.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['reallysimplesoftware'],
    'scripts': [],
    'name': 'reallysimplesoftware'
}

setup(**config)
