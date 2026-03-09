kamus = {
    "halo": "hai",
    "selamat pagi": "good morning",
    "selamat malam": "good night",
    "terima kasih": "thank you",
    "apa kabar": "how are you"
}

def translate(kata):
    kata = kata.lower()
    if kata in kamus:
        return kamus[kata]
    else:
        return "kata tidak ditemukan"

if __name__ == "__main__":
    print("Translator Indonesia -> Inggris")
    teks = input("Masukkan kata atau kalimat: ")
    hasil = translate(teks)
    print("Terjemahan:", hasil)