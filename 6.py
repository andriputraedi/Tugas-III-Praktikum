from turtle import pensize


print("                  program gaji pegawai         ")
print("_________________________________________________")


karyawan=(input("NAMA KARYAWAN :"))
anak=int(input("jumlah anak :"))

print("___________________________________________________________________________________")

gp=int(input( "* GAJI POKOK :"))
tks=gp * 20/100
print("* T.KESEJAHTERAAN :",tks)
tjl=gp*anak *10/100
print("* T.KELUARGA :",tjl)
pjk=gp*10/100
print("* PAJAK =",pjk)
print("________________________________________________________________________________________")

gk=gp+tks+tjl
print("GAJI KOTOR =",gk)
gb=gp+tks+tjl-pjk
print("GAJI BERSIH ",gb)