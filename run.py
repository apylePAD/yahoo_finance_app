import importlib
from yahoo_finance_app import config

base_path = config.BASE_PATH
app_run_input = config.APP_RUN_INPUT

if app_run_input == "all":
    for script_name in config.all_scripts:
       module = importlib.import_module(f'yahoo_finance_app.{script_name}')
else:
    module = importlib.import_module(f'yahoo_finance_app.{app_run_input}')
