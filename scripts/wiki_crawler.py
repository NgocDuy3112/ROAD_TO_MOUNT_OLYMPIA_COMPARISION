import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
from unidecode import unidecode
import re


def preprocess(table):
    if table.shape[0] == 5:
        table.columns = table.iloc[0]
        table.columns = [col.replace('0', ' ') for col in table.columns]
        table = table.iloc[1:].reset_index(drop=True)
    elif table.shape[0] == 4:
        pass
    else:
        print("Error: table shape is not 4 or 5")
        sys.exit(1)
    column_mapping = {col: unidecode(col) for col in table.columns}
    table.rename(columns=column_mapping, inplace=True)
    table.columns = [re.sub(r'\s+', '_', col) for col in table.columns]
    return table


if __name__ == "__main__":
    url = 'https://vi.wikipedia.org/wiki/%C4%90%C6%B0%E1%BB%9Dng_l%C3%AAn_%C4%91%E1%BB%89nh_Olympia_n%C4%83m_th%E1%BB%A9_23'
    dfs = pd.read_html(url, header=0)
    print(preprocess(dfs[54]))
