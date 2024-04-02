def sistem_manajemen_proses_rekrutmen_karyawan(umur, nilai_ipk):
    if umur > 21  and nilai_ipk >= 3.5:
        return True
    else:
        return False

umur = float(input("Masukkan umur Anda: "))
nilai_ipk = float(input("Masukkan nilai ipk: "))

if sistem_manajemen_proses_rekrutmen_karyawan(umur, nilai_ipk):
    print("Selamat! Anda memenuhi syarat untuk direkrut.")
else:
    print("Maaf, Anda tidak memenuhi syarat untuk direkrut.")