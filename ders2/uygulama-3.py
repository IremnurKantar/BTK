#kullanıcıdan harf girmesini isteyiniz "e" girerse erkek, "k" girerse kadın yazdırınız ekrana!
harf=input("Bir harf giriniz E/K:")

if harf=="E" or harf=="e":
    print("Erkek")
elif harf=="K"or harf=="k": #2. veya daha fazla şart olursa elif kullanılır
     print("Kadın")
else:
    print("Lütfen E veya K giriniz!")
print("Hoşçakalın...")
