from setuptools import setup, find_packages

setup(

    name='Bakery',
    version='0.1.0',

    author='Damian Czernous',
    author_email='damian.czernous@vonage.com',
    url='http://www.vonage.com',

    classifiers=[

        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: Free For Educational Use',

        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7'
    ],

    packages=find_packages(exclude=['docs', 'tests']),

    install_requires=['Flask', 'flask-RESTful'],

    test_suite='tests',
    tests_require=['mock']
)
