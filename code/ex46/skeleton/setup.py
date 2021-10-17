try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'ASIF HOSSAIN',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'hossainasif502@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'MyProjects'
}

setup(**config)