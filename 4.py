print("                PROGRAM MENGHITUNG PEMBELIAN ")
print("_____________________________________________________________")

harga=float(input("HARGA SATUAN  :"))
jum=float(input("JUMLAH PEMBELIAN  :"))
print("diskon : 10%")

discon=harga*0.1

print("total pembayaran :",harga*jum - discon)