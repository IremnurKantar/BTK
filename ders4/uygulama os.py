komut=input("Lütfen bir komut seçiniz: Dosya sil/Dosya oluştur")
if komut=="Dosya oluştur":
    dosya=input("Dosya adı:")
    import os
    os.mkdir(dosya)
elif komut=="Dosya sil":
    dosya1=input("Dosya adı:")
    import os
    os.rmdir(dosya1)