def hitung_diskon(total_belanja, punya_member):
    if punya_member:
        if total_belanja > 500000:
            diskon_persen = 0.20  # Diskon 20%
        else:
            diskon_persen = 0.10  # Diskon 10%
    else:
        if total_belanja > 500000:
            diskon_persen = 0.05  # Diskon 5%
        else:
            diskon_persen = 0.0   # Tidak ada diskon

    return diskon_persen

def main():
    # Input dari pengguna
    punya_member_input = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()
    total_belanja = float(input("Masukkan total belanja Anda (dalam rupiah): "))
    
    # Menentukan status member
    punya_member = True if punya_member_input == 'ya' else False

    # Menghitung diskon persentase
    diskon_persen = hitung_diskon(total_belanja, punya_member)

    # Menghitung jumlah diskon
    jumlah_diskon = total_belanja * diskon_persen

    # Menghitung total yang harus dibayar setelah diskon
    total_setelah_diskon = total_belanja - jumlah_diskon

    # Menampilkan hasil
    print(f"\nTotal belanja Anda: Rp {total_belanja:.2f}")
    print(f"Diskon yang didapat: {diskon_persen * 100:.0f}%")
    print(f"Jumlah diskon: Rp {jumlah_diskon:.2f}")
    print(f"Total yang harus dibayar setelah diskon: Rp {total_setelah_diskon:.2f}")

if __name__ == "__main__":
    main()