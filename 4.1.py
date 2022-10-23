n = 5 
nama = []
nilai = []
jumlahnilai = 0

for i in range(n):
    datanama = input("Masukan nama : ")
    datanilai = int(input("Masukan nilai : "))
    nama.append(datanama)
    nilai.append(datanilai)

print("---------------------------------------")
print("No          Nama       Nilai ")
print("---------------------------------------")
for j in range(n):
    print(j+1, "     ", nama[j], "      ",nilai[j])
    jumlahnilai = jumlahnilai + nilai[j]
    ratarata = jumlahnilai / n

print("Jumlah mahasiswa = ", n)
print("Rata - rata = ", ratarata)
    