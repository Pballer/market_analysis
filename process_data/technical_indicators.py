"""Add technical indicators to stocks prices."""

from finta import TA
from tqdm import tqdm


indicators = [(TA.CCI, {'period':30}),
              (TA.CCI, {'period':21}),
              (TA.CCI, {'period':14}),
              (TA.MACD, {}), 
              (TA.RSI, {'period':30}),
              (TA.RSI, {'period':21}),
              (TA.RSI, {'period':14}),
              (TA.ADL, {}),
              #(TA.EV_MACD, {})
             ]

def get_ta(ta_df):
    """Add technical indicators."""
    ta_list = []
    ta_df.set_index('date', inplace=True)
    for count, indicator in enumerate(indicators):
        try:
            #print(indicator)
            ta_results = indicator[0](ta_df, **indicator[1])
            ta_args = '_'.join([str(val) for val in indicator[1].values()])
            #ta_results = ta_results.add_suffix('{}_{}'.format(indicator[0].__name__, ta_args))
            if isinstance(ta_results, pd.Series):
                #if ta_results.name:
                new_name = (ta_results.name or indicator[0].__name__) + '_' + ta_args
                ta_results.rename(new_name, inplace=True)
                #print(ta_results.name)
            ta_list.append(ta_results)
        except NotImplementedError as e:
            print(e)
    return ta_list


def main():
    final_df = []
    for ticker in tqdm(aapl.tic.unique()):
        ta_df = aapl[aapl.tic == ticker]
        ta_list = get_ta(ta_df)
        final_df.append(ta_df.join(ta_list))
    return final_df

if __name__ == '__main__':
    main()
