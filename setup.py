from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name = 'saklient',
    version = '0.0.6',
    description = 'SAKURA Internet API Client Library',
    long_description=long_description,
    author='SAKURA Internet Inc.',
    author_email='dev-support-ml@sakura.ad.jp',
    py_modules = ["saklient"],
    url = 'http://cloud.sakura.ad.jp/',
    keywords = ['cloud'],
    license = "MIT",
    packages = [
        'saklient',
        'saklient.cloud',
        'saklient.cloud.enums',
        'saklient.cloud.errors',
        'saklient.cloud.models',
        'saklient.cloud.resources',
        'saklient.errors'
    ],
    install_requires = [
        'python-dateutil',
        'six'
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
