import pandas as pd
import datetime as dt

data=pd.read_excel('C:/Users/Dimas/Documents/Pyhton/alldata.xlsx')

tanggal = pd.datetime(2020, 1, 1, 0, 0)
tanggalakhir = pd.datetime(2020, 3, 1, 0, 0)
listtanggal=[]
while tanggal !=tanggalakhir:
    tanggalstr = dt.datetime.strftime(tanggal,'%Y%m%d %H:%M')
    listtanggal.append(tanggalstr)
    tanggal= tanggal + dt.timedelta(days=1)

data = data.set_index('tanggal')
data.reindex(listtanggal)

data.reindex(['(int)harga'], fill_value=0, axis = 'columns') 
alldata.to_excel('C:/Users/Dimas/Documents/Pyhton/alldata.xlsx', sheet_name='Data Bahan Pokok')