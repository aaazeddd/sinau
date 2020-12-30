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
