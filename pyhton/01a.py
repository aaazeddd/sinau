print("+-------------------------------------------+")
print("|  MENAMBAH MEGUBAH MENGHAPUS LIST ELEMENT  |")
print("+-------------------------------------------+")

print("\n=============================================")
nama_data = input("\nMasukkan nama data : ")
data = nama_data
data = []

print("\n=============PILIH MENU DI BAWAH=============")
print("+-------------------------------------------+")
print("|               1. Menambah                 |")
print("|               2. Mengubah                 |")
print("|               3. Menghapus                |")
print("+-------------------------------------------+")

choice = input("\nMasukkan pilihan : ")

print("\n=============================================")

if choice == '1' :
    tambah = int(input("\nJumlah data yang ingin dimasukkan : "))

    for x in range(tambah) :
        m = x+1
        a = input("Data ke-%d : " %m)
        data.append(a)

    print("\n=============================================")
    print("\nData %s :" % nama_data, data)


elif choice == '2' :
    print("\nData ke berapa yang ingin diubah?")

    u = int(input("Data ke : "))
    perubahan = input("Diubah menjadi : ")
    
    ubah = u-1
    data[ubah] = perubahan

    print("\n=============================================")
    print("\nData %s :" % nama_data, data)

elif choice == '3' :
    print("\nData ke berapa yang ingin dihapus?")

    h = int(input("Data ke : "))
    hapus = h-1
    del data[hapus]

    print("\n=============================================")
    print("\nData %s :" % nama_data, data)

else :
    print("\nKesalahan input.")
