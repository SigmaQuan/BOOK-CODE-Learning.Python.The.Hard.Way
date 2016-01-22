try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex51: .',
    'author': 'Quan Zhibin',
    'url': 'URL to get it at. ',
    'download_url': 'Where to download it. ',
    'author_email': 'quan.zhibin@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex51'],
    'scripts': [],
    'name': 'ex51'
}


setup(**config)
