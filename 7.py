print("                  kebutuhan karyaean         ")
print("______________________________________________")


gaji=int(input("gaji ="))
hutang=int(input("hutang ="))
bayar=gaji-hutang
print("sisa  =",bayar)
biaya=70/100* bayar
print("biaya sehari hari =",int (biaya))
tbg= 20/100*bayar
print("tabungan =",int (tbg))
inf= gaji-hutang-tbg-biaya
print("infak =",int (inf))