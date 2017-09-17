try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Hex Conveter',
    'author': 'Christopher M. Grass',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'cmgrassee@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['hexConverter'],
    'scripts': ['bin/hex.py'],
    'name': 'hexConverter'
}

setup(**config)
