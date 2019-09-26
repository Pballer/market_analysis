def format_sp_data():
    # Clean s&p 500 data for analysis.
    all_data = pd.read_csv('../data/sandp500_tickers.csv',
                           usecols=['datadate', 'tic', 'cshtrd', 'prcod', 'prccd', 'prchd', 'prcld'],
                           parse_dates=['datadate'],
                          )

    sandp = pd.read_csv('../data/sandp500.csv', parse_dates=['Date'])

    cols = [col.lower() for col in list(sandp.columns)]
    sandp.columns = cols

    sandp.drop('adj close', axis=1, inplace=True)



    all_data.dropna(inplace=True)

    all_data.columns = ['date', 'tic', 'volume', 'close', 'high', 'low', 'open']

    current_tickers = all_data[all_data.date == '2019-09-20'].tic.unique()

    current_tickers = [tic for tic in current_tickers if '.' not in tic]

    current_tickers = pd.DataFrame(current_tickers, columns=['tic'])

    current_sandp = pd.merge(all_data, current_tickers, how='inner')

    counts = current_sandp.tic.value_counts()

    keep_sandp = pd.DataFrame(counts[counts >= 2400].index, columns=['tic'])

    current_sandp = pd.merge(current_sandp, keep_sandp, how='inner')

    current_sandp.sort_values(by=['tic', 'date'], inplace=True)
    current_sandp.to_csv('sandp_cleaned.csv')
