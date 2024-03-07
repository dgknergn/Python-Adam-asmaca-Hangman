import sqlite3
import random
def joker_kullanimi(gizli_kelime, kelime, dogru_harfler):
    joker_hakki = True
    tahmin = input("JOKER kullanmak ister misiniz? (E/H): ").upper()
    if tahmin == "E":
        if joker_hakki:
            joker_hakki = False
            olmayan_harfler = [harf for harf in kelime if harf not in dogru_harfler] #doğru harflerde olmayan harfleri al olmayan_harflere at
            rastgele_harf = random.choice(olmayan_harfler) #olmayan harfler arasından rastgele bir harf seç
            indeks = kelime.index(rastgele_harf)    #denk gelen harfin indexini bul
            gizli_kelime[indeks] = rastgele_harf    # ve gizli kelimenin indexine denk gelen harfi ata
            print("JOKER kullandınız! Rastgele bir harf açıldı.")
            print(" ".join(gizli_kelime))
        else:
            print("JOKER hakkınız kalmadı.")
    else:
        print("JOKER kullanılmadı.")
def oyun_oyna():
    conn = sqlite3.connect('ogrencinonuz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT STR_KELIME FROM T_KELIME ORDER BY RANDOM() LIMIT 1")
    kelime = cursor.fetchone()[0]

    print("Kelime uzunluğu:", len(kelime))
    gizli_kelime = ['_' for _ in kelime]
    print(" ".join(gizli_kelime))

    hak = 8
    harfler = set()
    dogru_harfler = set()
    joker_kullanildi = False

    while hak>0 and '_' in gizli_kelime:
        if not joker_kullanildi:
            joker_kullanimi(gizli_kelime, kelime, dogru_harfler)
            joker_kullanildi = True

        tahmin = input("HARF GİRİNİZ: ").upper()

        if len(tahmin) ==1 and tahmin.isalpha():
            if tahmin in harfler:
                print("Bu harf zaten yazıyor")
                continue

            harfler.add(tahmin)

            if tahmin in kelime:
                dogru_harfler.add(tahmin)
                for i , harf in enumerate(kelime):
                    if tahmin == harf:
                        gizli_kelime[i] = tahmin
                        print("Doğru tahmin!")
                        print(" ".join(gizli_kelime))
            else:
                hak -= 1
                print("Yanlış tahmin! Kalan hak:", hak)
                adamıAs(hak)
                print(" ".join(gizli_kelime))

    if '_' not in gizli_kelime:
        print("Tebrikler, kelimeyi buldunuz:", kelime)
    else:
        print("Kaybettiniz! Doğru kelime:", kelime)

    conn.close()


def adamıAs(kalanhak):
    if kalanhak == 0:
        print("xxxxxxx")
        print("   |   ")
        print("   O   ")
        print("  /|\  ")
        print("   |   ")
        print("  / \  ")
        return "Hakkınız Kalmamıştır. OYUN BİTTİ!"
    elif kalanhak == 8:
        print("xxxxxxx")
        return "Hakkınız: " + str(kalanhak)
    elif kalanhak == 7:
        print("xxxxxxx")
        print("   |   ")
        return "Hakkınız: " + str(kalanhak)
    elif kalanhak == 6:
        print("xxxxxxx")
        print("   |   ")
        print("   O   ")
        return "Hakkınız: " + str(kalanhak)
    elif kalanhak == 5:
        print("xxxxxxx")
        print("   |   ")
        print("   O   ")
        print("  /   ")
        return "Hakkınız: " + str(kalanhak)
    elif kalanhak == 4:
        print("xxxxxxx")
        print("   |   ")
        print("   O   ")
        print("  / \  ")
        return "Hakkınız: " + str(kalanhak)
    elif kalanhak == 3:
        print("xxxxxxx")
        print("   |   ")
        print("   O   ")
        print("  /|\  ")
        return "Hakkınız: " + str(kalanhak)
    elif kalanhak == 2:
        print("xxxxxxx")
        print("   |   ")
        print("   O   ")
        print("  /|\  ")
        print("   |   ")
        return "Hakkınız: " + str(kalanhak)
    elif kalanhak == 1:
        print("xxxxxxx")
        print("   |   ")
        print("   O   ")
        print("  /|\  ")
        print("   |   ")
        print("  /   ")
        return "Hakkınız: " + str(kalanhak)

