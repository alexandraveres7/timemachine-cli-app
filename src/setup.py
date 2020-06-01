from setuptools import setup

setup(
    name='time_machine_cli',
    version='0.1',
    py_modules=['time_machine_cli'],
    install_requires=[],
    entry_points='''
        [console_scripts]
        time_machine_cli=time_machine_cli:timemachine
    ''',
)
