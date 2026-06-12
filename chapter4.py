print(f"kantor pengatur payout/bonus driver ojek online".upper())
print(f"===============================================".upper())

databasedriver = [4.8, 3.5, 4.6, 4.2, 2.0]

for rating in databasedriver:
    if rating >= 4.8:
        status_rating = "dapat bonus super (70% pendapatan)".upper()
    elif rating >= 4.5:
        status_rating = "dapat bonus standar (30% pendapatan)".upper()
    elif rating >= 4.0:
        status_rating = "tidak dapat bonus".upper()
    elif rating <4.0:
        status_rating = "peringatan akun driver!".upper()
    else:
        status_rating = "rating sangat buruk!".upper()
    print(f"Rata-rata Rating Driver : {rating:.2f} - {status_rating}")