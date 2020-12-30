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
