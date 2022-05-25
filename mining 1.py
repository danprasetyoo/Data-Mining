# Step 1: Menggabungkan Data Menjadi 1
import pandas as pd
import glob

# Menggabungkan Data Daftar Harga Bahan Pokok Januari & Februari
listfile=glob.glob('C:/Users/Dimas/Documents/Pyhton/Data*')
listfile=sorted(listfile)

alldata=pd.DataFrame()

for file in listfile :
    data=pd.read_csv(file)
    alldata=pd.concat([alldata,data], ignore_index=True)

# Menyimpan Gabungan Data Ke Folder
alldata.to_excel('C:/Users/Dimas/Documents/Pyhton/alldata.xlsx', sheet_name='Data Bahan Pokok')