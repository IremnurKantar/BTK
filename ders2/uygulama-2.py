#kullanıcıdan 5 tane sayı isteyerek en büyük sayıyı listeye atayarak bulunuz!
input("Hoşgeldiniz")
sayi1=input("1. sayıyı giriniz:")
sayi2=input("2. sayıyı giriniz:")
sayi3=input("3. sayıyı giriniz:")
sayi4=input("4. sayıyı giriniz:")
sayi5=input("5. sayıyı giriniz:")
sayilar=[]
sayilar.append(sayi1)
sayilar.append(sayi2)
sayilar.append(sayi3)
sayilar.append(sayi4)
sayilar.append(sayi5)
sayilar.sort()
print("Girmiş olduğunuz en büyük sayı:",sayilar[4])
sayilar.sort(reverse=True)
print("Girmiş olduğunuz en küçük sayı:",sayilar[4])
print("Girdiğiniz sayıların toplamı:",sayi1+sayi2+sayi3+sayi4+sayi5)
print("Girdiğiniz en büyük sayının 10 fazlası:",sayilar[0]+10)



