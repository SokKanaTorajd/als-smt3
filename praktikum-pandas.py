"""Series"""
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
karakter = pd.Series(data, index=['satu','dua','tiga','empat'])
print(karakter)

angka = pd.Series(np.array([20,54,24,78,23,67,23,98,32]))

print("nilai mean =",angka.mean())
print("nilai max = ",angka.max())
print("milai min = ",angka.min())


"""DataFrame"""
sou1 = {
        "country": ["Indonesia","Singapore","Malaysia"],
        "capital": ["Jakarta","Singapura","Putra Jaya"],
        "population" : [200000000,2000000,20000000]
}

sou2 = pd.DataFrame(sou1, index=['IDN','SGP','MLY'])
print(sou2)


#Importing csv
a = pd.read_csv('province-modify.csv')
print(a)
print(a.head())
print()
print(a.tail())


#JOIN DATAFRAME
df1 = pd.DataFrame({'key': ['K0','K1','K2','K3','K4','K5'],
                    'col1': ['a0','a1','a2','a3','a4','a5']})

print(df1)

df2 = pd.DataFrame({'key': ['K0','K1','K2'],
                    'col2': ['b1','b2','b3']})

print(df2)

joined = df1.join(df2.set_index('key'),on='key')
print(joined)


joined2 = df1.join(df2, lsuffix='_caller',rsuffix='_new')
print(joined2)

joined3 = df1.set_index('key').join(df2.set_index('key'))
print(joined3)
