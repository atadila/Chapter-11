from datetime import datetime
from datetime import date

def diffDate(date1, date2):
    return abs(date2-date1).days

def delta():
    d1 = date(2021,1,12)
    d2 = date(2021,1,20)
    #Tanggal yang akan dihitung
    result = diffDate(d2, d1)
    print('Selisih hari adalah', result)

delta()