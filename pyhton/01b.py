def judul() :
    print("+" ,43 * "-","+")
    print("|   MENAMBAH MEGUBAH MENGHAPUS LIST ELEMENT   |")
    print("+" , 43 * "-" , "+")

def menu() :
    print("")
    print("+",43 * "-","+")
    print("|",11 * " ","PILIH MENU DI BAWAH",11 * " ","|")
    print("+",43 * "-","+")
    print("|                1. Menambah                  |")
    print("|                2. Mengubah                  |")
    print("|                3. Menghapus                 |")
    print("|                4. Menampilkan data          |")
    print("|                5. Keluar                    |")
    print("+",43 * "-","+")

def pembatas() :
    print("")
    print(47 * "-")

def menambahkan() :
    tambah = int(input("\nJumlah data yang ingin dimasukkan : "))

    for x in range(tambah) :
        m = x+1
        a = input("Data ke-%d : " %m)
        data.append(a)

    pembatas()
    print("\nData %s :" % nama_data, data)

def mengubah() :
    print("\nData ke berapa yang ingin diubah?")

    u = int(input("Data ke : "))
    perubahan = input("Diubah menjadi : ")
        
    ubah = u-1
    data[ubah] = perubahan

    pembatas()
    print("\nData %s :" % nama_data, data)

def menghapus() :
    print("\nData ke berapa yang ingin dihapus?")

    h = int(input("Data ke : "))
    hapus = h-1
    del data[hapus]

    pembatas()
    print("\nData %s :" % nama_data, data)

def menampilkan_data() :
    print("data")

#---------------------------------------------------#

judul()

nama_data = input("\nMasukkan nama data : ")
data = nama_data
data = []

loop = True

while loop :
    menu()
    choice = input("\nMasukkan pilihan : ")
    
    pembatas()

    if choice == '1' :
        menambahkan()

    elif choice == '2' :
        mengubah()
        
    elif choice == '3' :
        menghapus()

    elif choice == '4' :
        menampilkan_data()

    elif choice == '5' :
        loop = False

    else :
        print("\nKesalahan input.")
