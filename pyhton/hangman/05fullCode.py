import random
import time

# ========= PERKENALAN ========== #
print("\nSelamat Datang di permainan Hangman by aaazeddd")
nama = input("Masukkan namamu : ")
print("Halo " + nama + "! Semoga Beruntung!")
time.sleep(2)
print("Permainan segera dimulai!\n Persiapkan dirimu untuk bermain Hangman!")
time.sleep(3)

'''
    import random = digunakan untuk mengambil secara acak pada []
    import time   = digunakan untuk mengambil waktu yang sedang berjalan di pc untuk menggunakan program
    time.sleep()  = digunakan untuk memberi jeda
'''

# ======== INISIALISASI ========= #
def main() :
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    words_to_guess = ["bulan", "matahari", "bumi", "mouse", "keyboard", "pot", "smartphone"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

'''
    global          = supaya bisa digunakan ke depannya tergantung pada bagaimana kita memanggilnya
    words_to_guess  = berisi kata-kata yang akan di tebak
    word            = variable untuk mengambil acak kata-kata pada variable words_to_guess
    length          = variable untuk menentukan panjang kata, menggunakan fungsi len()
    count           = diiskan 0 dan akan bertambah selanjutnya
    display         = untuk menampilkan garis sesuai dengan panjang kata
    already_guessed = berisi kata-kata yang sudah di tebak
'''

# ========== PLAY LOOP ========== #
def play_loop() :
    global play_game

    play_game = input("Ingin bermain lagi? [y = ya, n = tidak]\n")

    while play_game not in ["Y", "y", "N", "n"] :
       play_game = input("Ingin bermain lagi? [y = ya, n = tidak]\n")
    if play_game == "Y" or play_game == "y" :
        main()
    elif play_game == "N" or play_game == "n" :
        exit()

# MENGINISIALISASI SEMUA KONDISI YANG DIBUTUHKAN DALAM PERMAINAN #
def hangman() :
    global count
    global display
    global word
    global already_guessed
    global play_game

    limit = 5

    guess = input("Kata yang harus di tebak : " + display + " Masukkan huruf yang ingin ditebak : \n")
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9" :
        print("Kesalahan input. Masukkan huruf\n")
        hangman()
    
    elif guess in word :
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        
        print(display + "\n")
    
    elif guess in already_guessed :
        print("Coba masukkan huruf lain. \n")
    
    else :
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Salah menebak. " + str(limit - count) + " tebakkan lagi\n")

        elif count == 2:
            time.sleep(1)
            print("   _____  \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Salah menebak. " + str(limit - count) + " tebakkan lagi\n")

        elif count == 3:
           time.sleep(1)
           print("   _____  \n"
                 "  |     | \n"
                 "  |     | \n"
                 "  |     | \n"
                 "  |       \n"
                 "  |       \n"
                 "  |       \n"
                 "__|__\n")
           print("Salah menebak. " + str(limit - count) + " tebakkan lagi\n")

        elif count == 4:
            time.sleep(1)
            print("   _____  \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
            print("Salah menebak. " + str(limit - count) + " tebakkan lagi\n")

        elif count == 5:
            time.sleep(1)
            print("   _____  \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Salah menebak. Kamu digantung!!!\n")
            print("Katanya adalah :",already_guessed,word)
            play_loop()
    
    if word == '_' * length :
        print("Selamat! Kamu berhasil menebak katanya dengan benar!")
        play_loop()

    elif count != limit :
        hangman()

main()

hangman()
    

'''
    limit         = percobaan untuk menebak kata
    guess         = menyimpan huruf yang di input
    guess.strip() = menghapus huruf dari kata yang telah diberikan
'''
