def count_characters(string):
    # Inisialisasi dictionary untuk menyimpan jumlah kemunculan setiap karakter
    character_count = {}

    # Menghitung jumlah kemunculan setiap karakter dalam string
    for char in string:
        # Menggunakan metode get() untuk mendapatkan nilai awal 0 jika karakter belum ada dalam dictionary
        character_count[char] = character_count.get(char, 0) + 1

    return character_count

# Contoh string
string_input = "hello eduwork"

# Memanggil fungsi count_characters untuk menghitung jumlah kemunculan setiap karakter dalam string
character_count_result = count_characters(string_input)

# Menampilkan hasil
print("Jumlah kemunculan setiap karakter dalam string:" , string_input)
print(character_count_result)
