import pandas as pd
from yahoo_fin import stock_info as si
from yahoo_finance_app.config import BASE_PATH


def get_all_stock_tickers():

    # gather stock symbols from major US exchanges
    df1 = pd.DataFrame( si.tickers_sp500() )
    df2 = pd.DataFrame( si.tickers_nasdaq() )
    df3 = pd.DataFrame( si.tickers_dow() )
    df4 = pd.DataFrame( si.tickers_other() )

    print(df1)

    # convert DataFrame to list, then to sets
    sym1 = set( symbol for symbol in df1[0].values.tolist() )
    sym2 = set( symbol for symbol in df2[0].values.tolist() )
    sym3 = set( symbol for symbol in df3[0].values.tolist() )
    sym4 = set( symbol for symbol in df4[0].values.tolist() )

    # join the 4 sets into one. Because it's a set, there will be no duplicate symbols
    symbols = set.union( sym1, sym2, sym3, sym4 )

    # Some stocks are 5 characters. Those stocks with the suffixes listed below are not of interest.
    my_list = ['W', 'R', 'P', 'Q']
    del_set = set()
    sav_set = set()

    data = {
        'ticker_symbol':[]
    }

    for symbol in symbols:
        if len(symbol) > 4 and symbol[-1] in my_list:
            del_set.add(symbol)
        else:
            sav_set.add(symbol)
            data['ticker_symbol'].append(symbol)

    print( f'Removed {len(del_set)} unqualified stock symbols...' )
    print( f'There are {len(sav_set)} qualified stock symbols...' )

    df = pd.DataFrame(data)
    df = df.sort_values('ticker_symbol')
    df = df.fillna('n/a')
    df.to_csv(f'{BASE_PATH}/data_files/read_from_files/all_stock_tickers.csv', index=False)
    print(df.head())
    print(df.shape)


get_all_stock_tickers()