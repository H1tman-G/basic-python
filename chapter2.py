print(f"=========================================".upper())
print("Selamat Datang di Program #kotakitabersih".upper())
print(f"=========================================".upper())
#title phase



#input phase
username = input("Masukan Nama: ").lower()
usia_input = input("Masukan Usia: ")

#validation phase
if usia_input.isdigit():
    usia = int(usia_input)
else:
    print("Usia harus berupa angka.".upper())
    exit()

#library phase
is_age_valid = usia >= 16
is_name_valid = username == "marchel" #database username

#output phase
if is_age_valid and is_name_valid:
    print(f"Selamat Datang!".upper())
else:
    print(f"anda tidak terdaftar".upper())