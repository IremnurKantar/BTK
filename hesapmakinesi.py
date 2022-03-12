islem=input("Yapmak İstediğiniz İşlemi Seçiniz (+,-,*,/):")
sayi1=float(input("1. Sayıyı giriniz:"))
sayi2=float(input("2. Sayıyı giriniz:"))
if islem == "+":
   sonuc= sayi1 + sayi2
   print("İşleminizin sonucu:",sonuc)
elif islem == "-":
    sonuc = sayi1 - sayi2
    print("İşleminizin sonucu:",sonuc)
elif islem == "*":
    sonuc = sayi1 * sayi2
    print("İşleminizin sonucu:",sonuc)
elif islem == "/" and sayi2 != 0:
    sonuc = sayi1 / sayi2
    print("işleminizin sonucu:",sonuc)
else:
    print("Hatalı giriş yaptınız...!")