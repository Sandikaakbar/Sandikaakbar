def tentukan_nilai_huruf(nilai):
    """Fungsi untuk menentukan nilai huruf berdasarkan nilai yang diberikan."""
    if nilai > 90:
        return 'A'
    elif nilai > 80:
        return 'B'
    elif nilai > 70:
        return 'C'
    elif nilai > 60:
        return 'D'
    else:
        return 'E'

# Meminta input nilai dari pengguna
try:
    nilai = float(input("Masukkan nilai Anda (0-100): "))
    
    # Validasi input
    if 0 <= nilai <= 100:
        # Menentukan nilai huruf
        nilai_huruf = tentukan_nilai_huruf(nilai)
        # Menampilkan hasil
        print(f"Nilai huruf Anda adalah: {nilai_huruf}")
    else:
        print("Nilai harus berada dalam rentang 0 hingga 100.")
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")