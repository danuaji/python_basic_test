def reverse_words(sentence):
    # Memisahkan kata-kata dalam kalimat menjadi list
    words = sentence.split()
    # Membalik urutan kata-kata dalam list
    reversed_words = words[::-1]
    # Menggabungkan kata-kata yang sudah dibalik menjadi kalimat baru
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Contoh kalimat
kalimat = "mengerjakan soal test basic python di eduwork yang free "

# Memanggil fungsi reverse_words untuk membalik urutan kata-kata dalam kalimat
hasil = reverse_words(kalimat)

print("Kalimat sebelum dibalik urutan katanya:", kalimat)
# Menampilkan kalimat hasil pembalikan
print("Kalimat setelah dibalik urutan katanya:", hasil)
