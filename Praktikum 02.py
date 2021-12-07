from datetime import datetime
from datetime import date
from datetime import timedelta

try:
    myDoc = open('PerPus.txt', 'a')
    Daftar = []
    loop = 'y'
    while True:
        KMember = input('Masukkan Kode Member : ')
        NMember = input('Masukkan Nama Member : ')
        JBuku   = input('Masukkan Judul Buku  : ')
        date1 = datetime.date(datetime.now())
        date2 = date1 + timedelta(days=7)
        join = KMember+'|'+NMember+'|'+JBuku+'|'+str(date1)+'|'+str(date2)
        Daftar.append(join)
        loop = input('Tambah data lagi? (y/n) : ')
        if loop == 'y':
            continue
        else:
            break

    n = 0
    for data in Daftar:
        pinjam = str(Daftar[n])
        myDoc.write(pinjam+'\n')
        n += 1

    myDoc.close()
    
except FileNotFoundError:
    print('Maaf File Tidak Ditemukan :(')