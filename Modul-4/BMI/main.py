tinggi = float(input("Masukkan tinggi badan (dalam meter): "))
berat = float(input("Masukkan berat badan (dalam kilogram): "))

tinggi = tinggi / 100
bmi = berat / (tinggi ** 2)

print(f"skor BMI adalah :{bmi:.1f}")