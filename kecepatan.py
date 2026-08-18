# Program Hitung Kecepatan (v = s / t)
# Nama: Angelice Novena Octaviani

print(" PROGRAM HITUNG KECEPATAN 1")

jarak = float(input("Masukkan jarak (m): "))

# Pengecekan waktu tidak boleh 0 
waktu = float(input("Masukkan waktu (s): "))
while waktu == 0:
    print("Waktu tidak boleh 0 detik!")
    waktu = float(input("Masukkan waktu (s): "))

# Hitung kecepatan
kecepatan = jarak / waktu

print("\nHasil Perhitungan:")
print("Kecepatan (v) =", kecepatan, "m/s")