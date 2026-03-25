from setuptools import setup, find_packages

setup(
    name='Maxmsi',
    version='1.0.0',
    description='Malware detection system',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'maxmsi=maxmsi.cli:main',  # replace with your entry function
        ],
    },
)