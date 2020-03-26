# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:46:33 2020

@author: mehmet
"""

"""
Kelime Türetme oyunu, kullanıcıdan kelime istiyoruz, örneğin mehmet yazdı. yeni girilecek kelime mehmet kelimesinin son harfi ile başlamalı.
Ek olarak; bir kelime 2. defa yazılamaz yazılırsa hata mesajı verir
istenildiği zaman kelime torbası görüntülenebilir
istenildiği zaman kelime torbası sıfırlanabilir
istenildiği zaman çıkış yapılabilir
"""

kelime_torbasi = []

while True:
    
    print("Torbayı görmek için G ye basınız ")
    print(" Torbayı resetlemek için R ye basınız ")
    print(" Çıkmak için Ç ye basınız ")
    print("-----------------------------------------")
    
    kelime = input("torbaya at : ")
    
    if kelime in kelime_torbasi:
          print("HATA !!! BU KELİME DAHA ÖNCE GİRİLDİ : {}".format(kelime))
          print("----------------------------------------")
          
    elif kelime == "R":
        kelime_torbasi.clear()
        print(" Torba sıfırlandı ")
        print("----------------------------------------")
        
    elif kelime == "Ç":
        print(" Çıkış Yapıldı...")
        break

    elif kelime == "G":
        print("Torba Görüntüleniyor...")
        print(kelime_torbasi)
        print("----------------------------------------")
        
    
    else:
          print("yok!")
          kelime_torbasi.append(kelime)
          print(kelime_torbasi)
          print(" {} torbaya eklendi".format(kelime))
          print("-----------------------------------------")
          
      