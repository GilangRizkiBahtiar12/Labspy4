i=0
nama=[]
nim=[]
nilai_tugas=[]
nilai_uts=[]
nilai_uas=[]
nilai_akhir=[]

while True:
    s_nama=input("nama : ")
    nama.append(s_nama)
    s_nim=input("NIM : ")
    nim.append(s_nim)
    i_tugas=input("nilai tugas : ")
    nilai_tugas.append(i_tugas)
    i_uts=input("nilai UTS : ")
    nilai_uts.append(i_uts)
    i_uas=input("nilai UAS : ")
    nilai_uas.append(i_uas)

    i_nilai_akhir=(int(i_tugas)*0.30)+(int(i_uts)*0.35)+(int(i_uas)*0.35)
    nilai_akhir.append(i_nilai_akhir)

    lagi=""
    while lagi!="y" and lagi!="t":
        lagi=input("tamba Data (y/t) ?")
    i+=1
    if lagi=="t":
        break

print("                                                        Daftar Mahasiswa                                                                      ")
print("==============================================================================================================================================")
print("|  NO.  |      Nama        |       NIM         |          Tugas        |         UTS         |       UAS         |        Akhir              |")  
print("==============================================================================================================================================")
for n in range(i): 
    print("|      ",n+1,"     |       ",nama[n],"     |   ",nim[n],"     |     ",nilai_tugas[n],"    |   ",nilai_uts[n],"     |       ",nilai_uas[n],"       |    ",nilai_akhir[n],"      |")
    