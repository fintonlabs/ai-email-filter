file content

from setuptools import setup, find_packages

setup(
    name='email_classifier',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'nltk==3.6.2',
        'scikit-learn==0.24.2',
        'imaplib==3.3.0',
        'email==6.0.0',
    ],
    entry_points={
        'console_scripts': [
            'email_classifier=email_classifier:main',
        ],
    },
)