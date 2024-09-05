import os.path
import os
import pandas as pd
import sqlite3
from urllib.request import urlretrieve
import zipfile
import shutil


url = 'https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-ALL.zip/$FILE/PPR-ALL.zip'
zipfilename = 'PPR-ALL.zip'
filename = 'ppr.csv'
dbfilename = 'ppr.db'

urlretrieve(url, zipfilename)

with zipfile.ZipFile(zipfilename, 'r') as zip_ref:
    zip_ref.extractall('')
    extracted = zip_ref.namelist()
    
os.remove(zipfilename)

if (os.path.isfile(filename)):
    os.remove(filename)

os.rename(extracted[0], filename)

print(os.path.isfile(filename))

df = pd.read_csv(filename, delimiter=',', quotechar='"',encoding='cp1252')

df = df.drop('Not Full Market Price', axis='columns')
df = df.drop('Property Size Description', axis='columns')
df = df.drop('Description of Property', axis='columns')

df['Address'] = df['Address'].astype('str')
df['County'] = df['County'].astype('str')
df['Eircode'] = df['Eircode'].astype('str')

df['VAT Exclusive'] = df['VAT Exclusive'] .str.replace('Yes','1.125')
df['VAT Exclusive'] = df['VAT Exclusive'] .str.replace('No','1')
df['VAT Exclusive'] = df['VAT Exclusive'].astype('float')

df.rename(columns={'Price (€)': 'Price'}, inplace=True, errors="raise")
df['Price'] = df['Price'].str.replace('€','')
df['Price'] = df['Price'].str.replace(',','')
df['Price'] = df['Price'].astype('float')
df['Price'] = df['Price']*df['VAT Exclusive']
df['Price'] = df['Price'].astype('int')
df = df.drop('VAT Exclusive', axis='columns')

df.rename(columns={'Date of Sale (dd/mm/yyyy)': 'Date'}, inplace=True, errors="raise")
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df= df[::-1]
print(df.dtypes)
print(df.head)

conn = sqlite3.connect(dbfilename) 
print('Connected to DB')

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS register")
df.to_sql('regster', conn, if_exists='replace')

shutil.copy2(dbfilename, '.\\ppr\\')
