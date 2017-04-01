from setuptools import setup, find_packages

setup(
    name='selfnotify',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/menshikh-iv/selfnotify',
    license='MIT',
    author='Ivan Menshikh',
    author_email='menshikh.iv@gmail.com',
    description='Send notifications from python code to telegram',
    include_package_data=True
)
