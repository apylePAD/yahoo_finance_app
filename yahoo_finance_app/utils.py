import os
import datetime
import pandas as pd
import inquirer
import string
from yahoo_finance_app.config import BASE_PATH


class Script_Run_Logs:
    def __init__(self, script):
        self.script = script

    def script_start_log(self):
        print("-----------------------------------------------------")
        print(f"Script: {self.script}")
        print(f"Start Time: {datetime.datetime.now()}")

    def script_end_log(self):
        print(f"End Time: {datetime.datetime.now()}")
        print("-----------------------------------------------------")


class DF_Processor:
    def __init__(self, file_name):
        self.df = pd.read_csv(f"{base_path}/data_files/{file_name}.csv", low_memory=False)
        self.df.drop_duplicates(inplace=True)

    def fill_na(self, col_name, fill_value):
        self.df[col_name] = self.df[col_name].fillna(fill_value)

    def set_column_dtypes(self, col_dtype_dict):
        if not isinstance(col_dtype_dict, dict):
            raise TypeError("Expected a dictionary, got: {}".format(type(col_dtype_dict)))

        for col, dtype in col_dtype_dict.items():
            self.df[col] = self.df[col].astype(dtype)

    def df_col_list(self):
        return self.df.columns.tolist()

    def rename_columns(self, original_name, revised_name):
        self.df = self.df.rename(columns={original_name: revised_name})

    def write_to_csv(self, path):
        self.df.to_csv(path, index=False)


def get_ticker_letter():
    letter_choice = [
        inquirer.List(
            'letter',
            message="Select Letter",
            choices=string.ascii_uppercase,
        ),
    ]
    letter_choice = inquirer.prompt(letter_choice)
    letter_choice = letter_choice['letter']
    print(f"Pulling Stock Tickers + Company Names that start with: {letter_choice}")

    return letter_choice


def ticker_letter_folder(letter_passed):
    path = f'{BASE_PATH}/data_files/written_files/stock_historical_prices/{letter_passed}'
    try:
        os.mkdir(path)
        print(f'{letter_passed} | stock_historical_prices | Folder Successfully Created')
    except FileExistsError:
        print(f'{letter_passed} | stock_historical_prices | Folder Already Exists')
        pass
        
    path = f'{BASE_PATH}/data_files/written_files/stock_info/{letter_passed}'
    try:
        os.mkdir(path)
        print(letter_passed + ' - stock_info - Folder Successfully Created')
    except FileExistsError:
        pass
        print(letter_passed + ' - stock_info - Folder Already Exists')



def ticker_letter_slicer():
    def slicer_func(letter):

        data = {
            'ticker_symbol':[]
        }

        df = all_stocks_df()
        df = df.fillna('n/a')
        for row in df.itertuples():
            ticker = row.ticker_symbol
            if ticker == 'n/a':
                pass
            else:
                ticker_letter = ticker[0]
                if letter == ticker_letter:
                    data['ticker_symbol'].append(ticker)

        letter_df = pd.DataFrame(data)
        letter_df = letter_df.sort_values('ticker_symbol')
        letter_df.to_csv(base_path + '/data_files/read_from_files/list_of_all_' + letter + '_tickers.csv',index=False)
        print(letter_df)
    
    df = letters_df()
    for row in df.itertuples():
        letter = row.letter
        slicer_func(letter)


def stock_letter_df(letter):
    df = pd.read_csv(base_path + '/data_files/read_from_files/list_of_all_' + letter + '_tickers.csv')
    return df


def file_exists_status(letter,stock,company_name,api_call_type):
    if api_call_type == 'stock_info':
        file_path = base_path + '/written_files/stock_info/' + letter + '/stock_info_' + stock + '_' + company_name + '.csv'
    elif api_call_type == 'stock_price':
        file_path = base_path + '/written_files/stock_historical_prices/' + letter + '/stock_historical_prices_MAX_' + stock + '_' + company_name + '.csv'

    file_exists = os.path.exists(file_path)
    return file_exists


def file_date_checker(letter,stock,company_name,api_call_type):
    file_exists = file_exists_status(letter,stock,company_name,api_call_type)
    current_timestamp = time.time()
    if file_exists == True:
        date_updated = os.path.getctime(file_path)
        timestamp_delta_window = 3600 * 3
        timestamp_allowed = current_timestamp - timestamp_delta_window
        print(date_updated,timestamp_delta_window,timestamp_allowed)
        if date_updated <= timestamp_allowed:
            datetime_pull_allowed = 'yes'
        else:
            datetime_pull_allowed = 'no'
    else:
        datetime_pull_allowed = 'yes'
        print('File Not Found')

    return datetime_pull_allowed


def stock_names_df(letter):
    file_path = base_path + '/data_files/read_from_files/list_of_all_' + letter + '_tickers_with_company_names.csv'
    file_exists = os.path.exists(file_path)
    if file_exists == True:
        df = pd.read_csv(base_path + '/data_files/read_from_files/list_of_all_' + letter + '_tickers_with_company_names.csv')
    else:
        stock_data = {
            'ticker_symbol':[],
            'company_name':[]
        }
        df = pd.DataFrame(stock_data)
        df.to_csv(base_path + '/data_files/read_from_files/list_of_all_' + letter + '_tickers_with_company_names.csv',index=False)

    return df


        