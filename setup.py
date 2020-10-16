from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

test_requires = [
    'pytest'
]

setup(
    name='deferpy',
    version='1.0.1',
    author='David Buckley <david@davidbuckley.ca>',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'wrapt',
    ],
    extras_require={
        'dev': test_requires
    },
    tests_require=test_requires
)
