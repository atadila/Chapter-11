from datetime import datetime
from datetime import date

def diffDate(n):
    n = n.split('-')
    thn  = int(n[0])
    bln  = int(n[1])
    hari = int(n[2])
    date1 = datetime(thn, bln, hari)
    date2 = datetime.now()
    delta = date2 - date1
    return delta.days