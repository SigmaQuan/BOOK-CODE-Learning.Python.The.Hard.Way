try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex48: advanced user input.',
    'author': 'Quan Zhibin',
    'url': 'URL to get it at. ',
    'download_url': 'Where to download it. ',
    'author_email': 'quan.zhibin@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48'
}


setup(**config)
