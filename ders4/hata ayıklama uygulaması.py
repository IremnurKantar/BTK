#Kullanıcıdan sayı girmesini isteyin,sayı girmediğinde tekrar tekrar sayı girmesini isteyen,sayı
# girdiğinde de ekrana sayının karesini yazdıran program.

while True:
    try:
        sayi=int(input("Karesini almak istediğiniz sayıyı giriniz:"))
        break
    except ValueError:
        print("Lütfen sayı gir! Harf girme!")
print("Sayınızın karesi:",sayi**2)


