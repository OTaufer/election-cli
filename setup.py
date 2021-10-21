from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='cli-elections',
    version='0.2.0',
    author='Oldřich Taufer',
    author_email='O.Taufer@gmail.com',
    description='Application for displaying election results in the terminal.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'election = cli_elections.main:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False
)
