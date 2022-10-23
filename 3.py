

print("                PROGRAM MENGHITUNG PEMBELIAN ")
print("_____________________________________________________________")

harga=float(input("HARGA SATUAN  :"))
jumlah_pembelian=float(input("JUMLAH PEMBELIAN  :"))
diskon=harga * 0.1
print(" DISKON :",diskon)
print("Total pembayaran :",harga * jumlah_pembelian - diskon)