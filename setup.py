from distutils.core import setup
setup(
    name = 'saklient',
    version = '0.0.1',
    description = 'SAKURA Internet API Client Library',
    author='SAKURA Internet Inc.',
    author_email='k-furukawa@sakura.ad.jp',
    url = 'http://sakura.ad.jp/',
    packages = [
        'saklient',
        'saklient.cloud',
        'saklient.cloud.models',
        'saklient.cloud.resources'
    ]
)
