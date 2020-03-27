kelime_torbasi = []
sayac = 0
sonharf = " "
while True:    
    
    #print("Torbayı görmek için G ye basınız ")
    #print(" Torbayı resetlemek için R ye basınız ")
    #print(" Çıkmak için Ç ye basınız ")
    #print("-----------------------------------------")

    kelime = str(input("torbaya at : "))




    if sayac == 0 :
        ilkkelime =[]
        ilkkelime.append(kelime)
        ilkkelimesonharf = ilkkelime[0][-1]
        sayac +=1
        sonharf = ilkkelimesonharf
        print("Lütfen {} ile başlayan bir kelime giriniz ".format(ilkkelimesonharf))
        kelime_torbasi.append(kelime)
    else:

        if kelime in kelime_torbasi:
            print("Bu kelime listede mevcut başka bir kelime girmelisin")
        else:
            if kelime == 'g' or kelime == 'G':
                print(kelime_torbasi)
            elif kelime == 'ç' or kelime == 'Ç':
                print("oyundan cıkılıyor")
                break
            elif kelime == 'r' or kelime == 'R':
                kelime_torbasi.clear()
                print(kelime_torbasi)
                sayac = 0
            else:

                digerkelime = []
                digerkelime.append(kelime)
                digerkelimeilkharf = digerkelime[0][0]
                digerkelimesonharf = digerkelime[0][-1]
                if sonharf == digerkelimeilkharf:
                    print("Aferimmm ")
                    sonharf = digerkelimesonharf
                    print("{} ile başlayan yenii kelimeyi gir".format(sonharf))
                    kelime_torbasi.append(kelime)

                else:
                    print("Başarısız. {} ile başlayan bir kelime girmelisin.".format(sonharf))