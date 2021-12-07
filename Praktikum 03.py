from datetime import*
def diffDate(x):
    tgl = x.split("-")
    dateList = []
    for i in tgl:
        dateList.append(int(i))
    ystrdy = date(dateList[0], dateList[1], dateList[2])
    tdy = datetime.date(datetime.now())
    a = ystrdy - tdy
    b = a.days
    return b
file = open("PerPus.txt", "r")
isiFile = file.readlines()
kode = input("Masukkan Kode Member : ")
for i in range(len(isiFile)):
    if(kode in isiFile[i]):
        splitted = isiFile[i].split("|")
        status = "Ada"
        break
    else :
        status = "Tidak ada"
        continue
if(status == "Ada"):
    print("\nData Peminjaman Buku")
    print("Kode Member              : ", splitted[0])
    print("Nama Member              : ", splitted[1])
    print("Judul Buku               : ", splitted[2])
    print("Tanggal Mulai Peminjaman : ", splitted[3])
    print("Tanggal Maks Peminjaman  : ", splitted[4])
    print("Tanggal Pengembalian     : ", datetime.date(datetime.now()))
    trlmbt = diffDate(splitted[4])
    denda = 2000 * abs(trlmbt)
    if(trlmbt >= 0):
        print("Terlambat : 0 hari")
        print("Denda : 0")
        
    else:
        print("Terlambat : ", abs(trlmbt))
        print("Denda : ", denda)
else :
    print("Data Peminjaman Tidak Ditemukan")