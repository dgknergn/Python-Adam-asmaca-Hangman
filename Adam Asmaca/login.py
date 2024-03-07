import sqlite3

import menu

def login():
    conn = sqlite3.connect('ogrencinonuz.db')
    cursor = conn.cursor()

    login_hata = True
    while login_hata:

        kullanici_adi = input("Kullanıcı Adı: ").upper()
        sifre = input("Şifre: ")

        cursor.execute("SELECT * FROM T_USERS WHERE kullaniciAdi=? AND sifre=?",(kullanici_adi , sifre))

        user = cursor.fetchall()
        if user:
            print("Giriş başarılı!")
            login_hata = False
            menu.ana_menu()
            conn.close()
        else:
            print("Hatalı kullanıcı adı veya şifre!")


if __name__ == "__main__":
    login()
