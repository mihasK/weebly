from setuptools import setup

setup(name='weebly_api',
    version='0.1',
    description='Python functions to interface with Weebly Cloud Api',
    url='http://github.com/tkwon/weebly_api',
    author='T Kwon',
    author_email='tdkwon@gmail.com',
    license='MIT',
    packages=['weebly_api'],
    install_requires=[
        'requests',
    ],
    zip_safe=False)