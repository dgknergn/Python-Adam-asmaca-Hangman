import sqlite3
import string
def kelime_girisi():
    conn = sqlite3.connect('ogrencinonuz.db')
    cursor = conn.cursor()

    while True:
        kelime = input("Lütfen kelimeyi giriniz: ")

        if len(kelime) >= 5 and kelime.isalpha():
            kelime = kelime.upper()
            cursor.execute("INSERT INTO T_KELIME (STR_KELIME) VALUES (?)", (kelime,))
            conn.commit()
            print("Kelime eklendi!")
            break
        else:
            print("Lütfen en az 5 harf ve sadece harflerden oluşan bir kelime girin.")

    conn.close()

if __name__ == "__main__":
    kelime_girisi()