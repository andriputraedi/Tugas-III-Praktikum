print("           MENGHITUNG TAGIHAN TELEPON                     ")
print("____________________________________________________________")

print("DATA PELANGGAN ")
nama=(input("NAMA PELAGGAN  :"))
percakapan=int(input("PERCAKAPAN :"))
telpon=percakapan*1000
sms=int(input("SMS  :"))
pesan= sms * 300

print("TAGIHAN ")

print("ABONAME  : Rp. 20.000")
print("BIAYA PERCAKAPAN :",telpon)
print("BIAYA SMS :",pesan)
print("TOTAL TAGIHAN ",telpon+pesan+20000)