# ======== INISIALISASI ========= #
def main() :
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global clue_of_words
    global clue_choice

    words_to_guess = [
        "bulan", 
        "matahari", 
        "bumi", 
        "mouse", 
        "keyboard", 
        "pot", 
        "smartphone"
        ]
    clue_of_words = [
        "satelit alami bumi",
        "bintang di tata surya kita",
        "planet yang bisa di huni",
        "alat input komputer untuk menggerakkan cursor",
        "alat input komputer untuk mengetik",
        "tempat atau wadah untuk menanam tanaman",
        "gawai pintar"
    ]
    word = random.choice(words_to_guess)

    clue_choice = words_to_guess.index(word)

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
