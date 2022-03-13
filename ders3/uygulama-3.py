#kullancı adı ve şifre alınız.. kullanıcı adı olarak "admin" şifre olarak 123456 girilince "sisteme başarıyla
# giriş yaptınız" yazsın.. yanlış girildikçe "kullanıcı adı veya şifre hatalı" yazıp tekrar kullanıcı adı ve şifre
#sorsun

#kullanıcıadı=""
#şifre=()
#while  kullanıcıadı!="admin":
#    kullanıcıadı=input("kullanıcı adınız?")
#    input("Bilgiler hatalı.")
#while True :
#    kullanıcıadı=("admin")
#    input("Sisteme başarıyla giriş yaptınız.")
#    break
while True:
    kullaniciadı=input("Kullanıcı adınız:")
    sifre=input("Parolanız:")
    if kullaniciadı=="admin" and sifre=="123456":
        break
    else:
        print("Kullanıcı adı veya parola hatalı")
print("sisteme başarıyla giriş yaptınız..")