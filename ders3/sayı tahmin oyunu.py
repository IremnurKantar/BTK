tuttuğumsayı=5
while True:
        sayi=int(input("Tuttuğum sayıyı tahmin et.."))
        if sayi==tuttuğumsayı:
            int(input("Aferin tutturdun.."))
            break
        elif sayi<tuttuğumsayı:
            int(input("Tahmininizi büyütün.."))
        elif sayi>tuttuğumsayı:
            int(input("Tahmininizi küçültün.."))