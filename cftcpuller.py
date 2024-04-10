import pandas as pd 
import requests
from zipfile import ZipFile
from io import BytesIO
import datetime

#high bound exclusive in python
years = [i for i in range(2010,2021)]


def download_extract_zip(link): 
    r = requests.get(link,stream=True) 
    zip_file = ZipFile(BytesIO(r.content)) 
    df = pd.read_csv(BytesIO(zip_file.read(zip_file.namelist()[0]))) 
    return df  

for year in years:
    df = download_extract_zip(f'https://www.cftc.gov/files/dea/history/fut_fin_txt_{year}.zip')
    df.to_csv(f'finfut_{year}.csv',index=False)