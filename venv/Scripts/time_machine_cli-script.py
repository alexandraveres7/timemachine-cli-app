#!C:\Users\Alexandra\PycharmProjects\awesome-cli-app\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'time-machine-cli','console_scripts','time_machine_cli'
__requires__ = 'time-machine-cli'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('time-machine-cli', 'console_scripts', 'time_machine_cli')()
    )
