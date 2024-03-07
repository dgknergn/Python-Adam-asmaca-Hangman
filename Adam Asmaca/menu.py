import KelimeGir
from login import login
from KelimeGir import kelime_girisi
def ana_menu():

    while True:
        print("ADAM ASMACA OYUNUNA HOSGELDINIZ")
        print("1-KELIME GIRISI")
        print("2-OYUN OYNA")
        print("Q-PROGRAMI SONLANDIR")

        secim = input("Seçiminizi yapınız: ")
        if secim == '1':

            KelimeGir.kelime_girisi()
        elif secim == '2':
            from Oyun import oyun_oyna
            oyun_oyna()
        elif secim == 'Q' or 'q':
            print("Görüşmek Üzere")
            exit()
        else:
            print("Geçersiz seçim!")
