from setuptools import setup, find_packages

setup(
    name='src',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points='''
        [console_scripts]
        time_machine_cli=src.cli.time_machine_cli:timemachine
    ''',
)
