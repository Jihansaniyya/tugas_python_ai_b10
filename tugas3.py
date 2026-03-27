"""Tugas Python dasar: variabel, string, matematika, list, dan input user."""

# 1) Deklarasi variabel dengan tipe data berbeda
nama_kelas = "Python AI B10"          # string
jumlah_siswa = 25                      # integer
nilai_rata_rata = 88.75                # float
kelas_aktif = True                     # boolean
daftar_hobi = ["membaca", "coding", "musik", "olahraga", "traveling"]  # list

print("=== Deklarasi Variabel dan Tipe Data ===")
print("nama_kelas:", nama_kelas)
print("jumlah_siswa:", jumlah_siswa)
print("nilai_rata_rata:", nilai_rata_rata)
print("kelas_aktif:", kelas_aktif)
print("daftar_hobi:", daftar_hobi)

# 2) Manipulasi string
print("\n=== Manipulasi String ===")
teks_1 = "Belajar"
teks_2 = "Python"
gabungan = teks_1 + " " + teks_2

print("Gabungan string:", gabungan)
print("Panjang string:", len(gabungan))
print("Huruf besar:", gabungan.upper())
print("Huruf kecil:", gabungan.lower())

# 3) Operasi matematika sederhana
print("\n=== Operasi Matematika Sederhana ===")
angka_a = 20
angka_b = 6

print("Penjumlahan (+):", angka_a + angka_b)
print("Pengurangan (-):", angka_a - angka_b)
print("Perkalian (*):", angka_a * angka_b)
print("Pembagian (/):", angka_a / angka_b)
print("Pembagian bulat (//):", angka_a // angka_b)
print("Sisa bagi (%):", angka_a % angka_b)

# 4) List dan akses elemen
print("\n=== List dan Akses Elemen ===")
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]
print("List awal:", buah)
print("Elemen pertama:", buah[0])
print("Elemen ketiga:", buah[2])

buah.append("semangka")
print("Setelah append('semangka'):", buah)

buah.remove("jeruk")
print("Setelah remove('jeruk'):", buah)

buah_terakhir = buah.pop()
print("Item yang di-pop:", buah_terakhir)
print("List akhir:", buah)

# 5) Penggunaan input dari user
print("\n=== Input dari User ===")
nama_user = input("Masukkan nama Anda: ")
umur_user = input("Masukkan umur Anda: ")

print(f"Halo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
