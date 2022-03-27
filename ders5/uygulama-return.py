#kendisine gönderilen dikdörtgenin alanını ve çevresini hesaplayan iki ayrı fonksiyon yazınız. Kullanıcıdan aldığınız
# değere göre alanı ve çevreyi ekrana yazdırınız.
def alan(a,b):
    return a*b
def cevre(a,b):
    return (a+b)*2
a=int(input("Dikdörtgenin kısa kenarının uzunluğu:"))
b=int(input("Dikdörtgenin uzun kenarının uzunluğu:"))
print("Dikdörtgenin alanı:",alan(a,b))
print("Dikdörtgenin çevresi:",cevre(a,b))