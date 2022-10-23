from turtle import pen


dataA =[0.5,1.0,1.5,2.0]
dataB=[800,1600,2400,3200,]

print('''
___________________________________________
|         satuan       |       harga       |
____________________________________________''')

for x in range(len(dataA)):
    isi=str(dataA[x])
    print('|   '+isi,end='')
    for y in range (20-3-len(isi)):
        print (' ',end='')
isi1=str(dataB[x])
print('|   '+isi1,end='')
for y in range (20-5-len(isi1)):
    print(' ',end='')
print("_______________________________________")