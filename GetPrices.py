import pandas as pd
import time

from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df

valor_bitcoin = get_bitcoin_df()
valor_commodities = get_commodities_df()
    

while True:

    df=pd.concat([get_bitcoin_df(), get_commodities_df()], ignore_index=True)
    print(df)

time.sleep(60)