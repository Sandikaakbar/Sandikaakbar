#percabangan
#struktur
"""
    1.if -nya
    2.punya kondisi
    3.punya aksi
"""
nama = input ("masukkan nama : ")

#percabangan yang inline
if nama == "sandika" : print ("selamat datang")
print("terima kasih")

#percabangan indentasi
if nama == "sandika" :
    print("selamat datang")
    print("selamat datang python")
print("bukan bagian percabangan")

#percabangan 1 kondisi 2 aksi
#pakai tanda kunci 'else'

if nama == "sandika" :\
    print("selamat datang")
else:
    print(f"anda {nama}, bukan adam ")
print("terima kasih")