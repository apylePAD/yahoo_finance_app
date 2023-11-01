import yfinance as yf
import pandas as pd
import inquirer
from datetime import datetime,date,timedelta
from yahoo_finance_app import config
from yahoo_finance_app.utils import get_ticker_letter

base_path = config.BASE_PATH

ticker_letter = get_ticker_letter()
print(ticker_letter)

class Stock_Ticker:
    def __init__(self, ticker_letter):
        self.ticker_letter = ticker_letter
    
    def stock_data(self):







# letter_input = input('SELECT LETTERS TO RUN ( 1. all / 2. single_letter ) :')
# if letter_input == '1':
#     letter_input = 'all'
# elif letter_input == '2':
#     letter_input = 'single_letter'

#     df = letters_df()
#     letters_list = list(df['letter'])
#     letter_selection = [
#         inquirer.List('letter',
#                 message="Select Letter",
#                 choices=letters_list,
#             ),]
#     options = inquirer.prompt(letter_selection)
#     letter_selected = options['letter']


# def stock_info_func(letter):

#     error_data = {
#         'ticker_symbol':[]
#     }

#     def stock_info(ticker_letter,stock_passed):

#         # file_exists = file_exists_status(letter,ticker,'stock_info')
#         name_df = stock_names_df(letter)
        
#         stock_data = {
#             'ticker_symbol':list(name_df['ticker_symbol']),
#             'company_name':list(name_df['company_name'])
#         }

#         ticker_list = list(name_df['ticker_symbol'])
#         if stock_passed not in ticker_list:
#             stock = yf.Ticker(stock_passed)
#             results = stock.info
           
#             datetime_pull_allowed = 'yes'
#             # datetime_pull_allowed = file_date_checker(ticker_letter,stock_passed,'stock_info')
#             if datetime_pull_allowed == 'yes':
#                 try:
#                     company_name = results['shortName']

#                     list_of_keys = results.keys()
#                     list_of_values = list(map(results.get,list_of_keys))

#                     df = pd.DataFrame(list(zip(list_of_keys,list_of_values)),columns=['key','value'])
#                     df.to_csv(base_path + '/data_files/written_files/stock_info/' + ticker_letter + '/stock_info_' + stock_passed + '_' + company_name + '.csv',index=False)

#                     stock_data['ticker_symbol'].append(stock_passed)
#                     stock_data['company_name'].append(company_name)
                    
#                     print(ticker_letter,stock_passed,company_name)
#                     name_df = pd.DataFrame(stock_data)
#                     name_df.to_csv(base_path + '/data_files/read_from_files/list_of_all_' + letter + '_tickers_with_company_names.csv',index=False)
#                     print(name_df)
#                 except:
#                     error_data['ticker_symbol'].append(stock_passed)
#                     print('ERROR - ',stock_passed)
#             else:
#                 print(stock_passed + ' - Stock Info Pulled Too Recently')
#         else:
#             pass
        

#     def stock_letter_looper(letter):
#         counter = 0
#         df = stock_letter_df(letter)
#         ttl_stocks = len(df)
#         for row in df.itertuples():
#             ticker = row.ticker_symbol
#             stock_info(letter,ticker)
#             pct_complete = (counter / ttl_stocks) * 100
#             pct_complete = "{0:.3f}%".format(pct_complete)
#             counter += 1
#             print(pct_complete)

#     stock_letter_looper(letter)

#     error_df = pd.DataFrame(error_data)
#     error_df.to_csv(base_path + '/data_files/written_files/list_of_' + letter + '_tickers_with_errors.csv',index=False)
#     print(error_df)



# if letter_input == 'all':
#     df = letters_df()
#     for row in df.itertuples():
#         letter = row.letter
#         ticker_letter_folder(letter)
#         stock_info_func(letter)
# elif letter_input == 'single_letter':
#     ticker_letter_folder(letter_selected)
#     stock_info_func(letter_selected)







