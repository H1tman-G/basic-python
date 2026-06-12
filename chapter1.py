username = input(" Masukan Nama  : ").lower()
usia = int(input(" Masukan Usia  : "))

status_usia = "Belum Cukup Umur "
if usia >= 16:
    status_usia = "Cukup Umur "

status_nama = "Nama Tidak Valid "
if username == "budi": #database username
    status_nama = "Nama Valid "

print(f"Nama : {username} - {status_nama}".upper())
print(f"Usia : {usia} - {status_usia}".upper())