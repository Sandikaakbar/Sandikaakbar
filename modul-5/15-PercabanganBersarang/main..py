# percabangan bersarang / Nested IF

# kalkulator
# +,-,x,/,mood,//,pangkat (exsponen)

print(20*"=")
print("kalkulator sederhana")
print(20*"=")

angka_1 = float(input("masukkan bilangan 1 = "))
operator = input("operator (+,-,x,/,%,//,**,) = ")
angka_2 = float(input("masukkan bilangan 2 = "))

# percabangan bersarang (elif Statment)

if operator == '+' :
    hasil = angka_1 + angka_2
    print(f'Hasilnya adalah = {hasil}')
elif operator == '-' :
    hasil = angka_1 - angka_2
    print(f'Hasilnya adalah = {hasil}')
elif operator == 'x' or operator == '*':
    hasil = angka_1 * angka_2
    print(f'Hasilnya adalah = {hasil}')
elif operator == '/' :
    hasil = angka_1 / angka_2
    print(f'Hasilnya adalah = {hasil}')
elif operator == '%' or operator == 'mood':
    hasil = angka_1 % angka_2
    print(f'Hasilnya adalah = {hasil}')
elif operator == '//' :
    hasil = angka_1 // angka_2
    print(f'Hasilnya adalah = {hasil}')
elif operator == '**' :
    hasil = angka_1 ** angka_2
    print(f'Hasilnya adalah = {hasil}')    
else:
    print(f'Operator {operator} tidak ditemukan!')

print("Terima Kasih")