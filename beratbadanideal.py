tinggi_badan = int(input("Masukan Tinggi Badan Anda : "))
meter = int(tinggi_badan) / 100
berat_badan = int(input("Masukan Berat Badan Anda : "))
hasil = berat_badan / (meter * meter)
if hasil < 18.5 :
    print("kurus")
elif 18.5 <= hasil <= 24.9 :
    print("normal")
elif 25 <= hasil <= 29.9 :
    print("Overweight")
elif hasil >30 :
    print("Obesitas") 