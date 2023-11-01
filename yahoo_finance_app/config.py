import os
import platform
import getpass
import inquirer

current_system = platform.system()
current_user = getpass.getuser()

if current_system == "Darwin":
    if current_user == "apyle_imac":
        BASE_PATH = "/Users/apyle_imac/Documents - iMac/PAD/Python/custom_apps/yahoo_finance_app/yahoo_finance_app"
    elif current_user == "andrewpyle":
        BASE_PATH = "/Users/andrewpyle/Documents/Documents - MacBook Air/PAD/Python/custom_apps/yahoo_finance_app/yahoo_finance_app"
    else:
        print("Current user not recognized. Please add user to config.py")
        BASE_PATH = None
else:
    print("Current system not recognized. Please add system to config.py")
    BASE_PATH = None

script_dir = os.path.dirname(os.path.abspath(__file__))
all_scripts = [f.replace('.py', '') for f in os.listdir(script_dir) if f.endswith('.py') and f not in ['__init__.py', 'config.py', 'run.py', 'utils.py']]

app_run_choices = ['all'] + all_scripts
app_run_choices.sort()
app_run_choices = [
    inquirer.List('APP_RUN_CHOICE',
        message='Which portion(s) of the app do you want to run?',
        choices=app_run_choices),
]
APP_RUN_INPUT = inquirer.prompt(app_run_choices)["APP_RUN_CHOICE"]

