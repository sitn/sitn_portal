import os

from setuptools import setup, find_packages

requires = [
    'c2c.template',
    'plaster_pastedeploy',
    'psycopg2',
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid-mako',
    'pyramid_retry',
    'pyramid_tm',
    'pyyaml',
    'SQLAlchemy',
    'sqlahelper',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='sitn_portal',
    version='0.0',
    description='sitn_portal',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = sitn_portal:main',
        ],
        'console_scripts': [
            'initialize_sitn_portal_db = sitn_portal.scripts.initializedb:main',
        ],
    },
)
