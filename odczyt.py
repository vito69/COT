
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # szukane nazwy
    euro_fx = 'EURO FX - CHICAGO MERCANTILE EXCHANGE'
    leverage_long = 'Lev_Money_Positions_Long_All'
    leverage_short = 'Lev_Money_Positions_Short_All'
    
    # otwieranie xls
    df = pd.read_excel('FinFutYY.xls') 

    # szukanie numeru indeksu po nazwie '\n'
    firstEUR = np.where(df == euro_fx)[0][0] 
    #firstlong = df.columns.get_loc(leverage_long) 
    #firstshort = df.columns.get_loc(leverage_short)
    
    # odczytywanie i formatowanie wartości
    headerlong = leverage_long.replace('_', ' ')
    headershort = leverage_short.replace('_', ' ')
    data = str(df.loc[firstEUR]['Report_Date_as_MM_DD_YYYY'])[0:10]
    row_nazwa = df.loc[firstEUR]['Market_and_Exchange_Names']
    long_euro = df.loc[firstEUR][leverage_long]
    short_euro = df.loc[firstEUR][leverage_short]
    difference = long_euro - short_euro
    
    # wyświetlane w terminalu
    print(data)
    print(row_nazwa)
    print(headerlong, '=', long_euro)
    print(headershort, '=', short_euro)
    print('long - short =', difference)
    
    # wykres
    helong = ' = '.join([headerlong.split(' ')[3], str(long_euro)])
    heshort = ' = '.join([headershort.split(' ')[3], str(short_euro)])
    heroznica = ''.join(['Różnica =', str(difference)])
    height = [long_euro, short_euro, abs(difference)]
    labels = [helong, heshort, heroznica]
    params = {"text.color" : "ffffaa",
          "xtick.color" : "7b3f00",
          "ytick.color" : "7b3f00"}
    plt.style.use("dark_background")
    plt.rcParams.update(params)
    barlist = plt.bar(labels, height)
    barlist[0].set_color('#7b3f00')
    barlist[1].set_color('#7b3f00')
    barlist[2].set_color('#7b3f00')
    plt.title(row_nazwa[0:7] + ' ' + str(data) + '\n ' + leverage_long[0:18].replace('_', ' '))
    plt.show()

if __name__ == '__main__':
    main()

