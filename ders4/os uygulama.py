#while True:
#    try:
#        import os
#        os.mkdir("elma")
#    except:
#            print("Genel hata oluştu.")
#            break
os.rmdir("elma")
import os
for i in range(1,11):
    os.mkdir("elma"+str(i))



