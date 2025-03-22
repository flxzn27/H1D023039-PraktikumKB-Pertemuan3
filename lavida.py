import random
import numpy as np

print("===== SELAMAT DATANG DI TOKO LA VIDA =====")

# Struktur Data
tuple_jenis = ["Halli Galli", "Yut Nori", "Gonggi", "Ddakji"]
list_harga = [65000, 25000, 10000, 15000]
set_bonus = {"Permen Lolipop", "Tempat Pensil", "Penghapus"}

# Menampilkan daftar harga
print("\n== LIST HARGA ==")
for i in range(len(tuple_jenis)):
    print(f"{i+1}. {tuple_jenis[i]} - Rp {list_harga[i]:,}")

# Input jumlah item yang dibeli
total_harga = 0
keranjang = [0] * len(tuple_jenis)
while True:
    pilihan = input("Masukkan nomor produk yang ingin dibeli (atau ketik 'selesai' untuk checkout): ")
    if pilihan.lower() == 'selesai':
        break
    
    if not pilihan.isnumeric() or not (1 <= int(pilihan) <= len(tuple_jenis)):
        print("Pilihan tidak valid, silakan coba lagi.")
        continue
    
    index = int(pilihan) - 1
    jumlah = input(f"Masukkan jumlah {tuple_jenis[index]} yang ingin dibeli: ")
    
    keranjang[index] += int(jumlah)
    
    print(f"{tuple_jenis[index]} x{jumlah} ditambahkan ke keranjang. Total sementara: Rp {sum(keranjang[i] * list_harga[i] for i in range(len(tuple_jenis))):,}")

# Menampilkan struk belanja
total_harga = sum(keranjang[i] * list_harga[i] for i in range(len(tuple_jenis)))
print("\n===== STRUK BELANJA =====")
for i in range(len(keranjang)):
    if keranjang[i] > 0:
        print(f"{tuple_jenis[i]} x{keranjang[i]}")
print(f"Total Harga: Rp {total_harga:,}")

# Menentukan bonus jika total harga lebih dari 40.000
if total_harga > 40000:
    bonus_acak = random.choice(list(set_bonus))
    print(f"Selamat! Anda mendapatkan bonus: {bonus_acak}")
    print("Bonus telah ditambahkan ke keranjang Anda.")

print("\nTerima kasih telah berbelanja di La Vida! Sampai jumpa lagi.")