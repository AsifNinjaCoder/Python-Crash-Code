try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Advance User Input',
    'author': 'ASIF HOSSAIN',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'hossainasif502@gmail.com',
    'version': '0.2',
    'install_requires': ['nose'],
    'packages': ['Exercise49'],
    'scripts': [],
    'name': 'MyProjects_v2.0'
}

setup(**config)