def Enkripsi(pesan):
    enkripsi = ""
    for karakter in pesan:
        if karakter.isalpha():
            key = 3
            unicode = ord(karakter)
            unicode_key = unicode + key
            if karakter.isupper():
                if unicode_key > ord("Z"):
                    unicode_key -= 26
            else:
                if unicode_key > ord("z"):
                    unicode_key -= 26
            enkripsi_pesan = chr(unicode_key)
            enkripsi += enkripsi_pesan
        else:
            enkripsi += karakter
    return enkripsi

def Deskripsi(pesan):
    deskripsi = ""
    for karakter in pesan:
        if karakter.isalpha():
            key = 3
            unicode = ord(karakter)
            unicode_key = unicode - key
            if karakter.isupper():
                if unicode > ord("Z"):
                    unicode_key -= 26
                elif unicode < ord("A"):
                    unicode_key += 26
            else:
                if unicode > ord("z"):
                    unicode_key -= 26
                elif unicode_key < ord("a"):
                    unicode_key += 26
            Deskripsi_Pesan = chr(unicode_key)
            deskripsi += Deskripsi_Pesan
        else:
            deskripsi +=karakter
    return deskripsi

print("Nama     : Aditya Rizky Darmawan")
print("Kelas    : 3C Informatika")
print("NPM      : 2210631170109")
print("")

print("Menu Pilihan :")
print("1. Enkripsi Pesan")
print("2. Deskripsi Pesan yang di Enkripsi")
pil = input("Masukkan Pilihan : ")

if pil == "1":
    pesan = input("Masukkan Pesan: ")
    print("Pesan Enkripsi : ", Enkripsi(pesan))
else:
    pesan = input("Masukkan Enkripsi Pesan: ")
    print("Deskripsi Pesan yang terenkripsi: ", Deskripsi(pesan))