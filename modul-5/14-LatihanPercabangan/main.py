# Meminta input total belanja dari pengguna
total_belanja = float(input("Masukkan total belanja Anda (dalam ribu): "))

# Percabangan untuk menentukan hadiah
if total_belanja > 500000:
    hadiah = "Anda mendapatkan mouse dan keyboard."
else:
    hadiah = "Anda hanya mendapatkan gantungan kunci."

# Menampilkan hasil
print(hadiah)
