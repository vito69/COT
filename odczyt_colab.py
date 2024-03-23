
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # szukane nazwy
    euro_fx = 'EURO FX - CHICAGO MERCANTILE EXCHANGE'
    leverage_long = 'Lev_Money_Positions_Long_All'
    leverage_short = 'Lev_Money_Positions_Short_All'
    leverage_spread = 'Lev_Money_Positions_Spread_All'

    # otwieranie xls
    df = pd.read_excel('FinFutYY.xls') 

    # szukanie numeru indeksu po nazwie '\n'
    firstEUR = np.where(df == euro_fx)[0][0] 
    #firstlong = df.columns.get_loc(leverage_long) 
    #firstshort = df.columns.get_loc(leverage_short)
    
    # odczytywanie i formatowanie wartości
    headerlong = leverage_long.replace('_', ' ')
    headershort = leverage_short.replace('_', ' ')
    headerspread = leverage_spread.replace('_', ' ')
    data = str(df.loc[firstEUR]['Report_Date_as_MM_DD_YYYY'])[0:10]
    row_nazwa = df.loc[firstEUR]['Market_and_Exchange_Names']
    long_euro = df.loc[firstEUR][leverage_long]
    short_euro = df.loc[firstEUR][leverage_short]
    spread = df.loc[firstEUR][leverage_spread]
    difference = long_euro - short_euro
    dfw = pd.DataFrame({'Long':[long_euro], 'Short':[short_euro], 'Spread':[spread], 'Difference':[difference]})
    
    # wyświetlane w terminalu
    print(data)
    print(row_nazwa)
    print(headerlong, '=', long_euro)
    print(headershort, '=', short_euro)
    print(headerspread, '=', spread)
    print('long - short =', difference)
    dfw.plot(kind = 'bar', title = row_nazwa + '-' + data)

if __name__ == '__main__':
    main()

