# Program Konversi Suhu Fisika
# Nama: Angelice Novena Octaviani

print(" PROGRAM KONVERSI SUHU FISIKA ")

# 1. Input Suhu Celsius
celsius = float(input("Masukkan suhu Celsius: "))

# 2. Proses Konversi Rumus
reamur = (4 / 5) * celsius
fahrenheit = ((9 / 5) * celsius) + 32
kelvin = celsius + 273.15

# 3. Tampilkan Hasil
print("\nHasil Konversi:")
print("Suhu Reamur     :", reamur, "R")
print("Suhu Fahrenheit :", fahrenheit, "F")
print("Suhu Kelvin     :", kelvin, "K")