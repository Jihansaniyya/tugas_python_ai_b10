# Bagian 1: contoh variabel dengan tipe data yang berbeda.
nama_kelas = "Python AI B10" ##String
jumlah_siswa = 25 ##Integer
nilai_rata_rata = 88.75 ##Desimal Float
kelas_aktif = True ##Boolean
hobi = ["membaca", "coding", "musik", "olahraga", "traveling"] ##List

print("Data variabel:")
print("kelas:", nama_kelas)
print("jumlah siswa:", jumlah_siswa)
print("nilai rata-rata:", nilai_rata_rata)
print("kelas aktif:", kelas_aktif)
print("hobi:", hobi)

# Bagian 2: manipulasi string sederhana.
kata1 = "Belajar"
kata2 = "Python"
teks = kata1 + " " + kata2

print("\nManipulasi string:")
print("gabungan:", teks)
print("panjang:", len(teks))
print("upper:", teks.upper())
print("lower:", teks.lower())

# Bagian 3: operasi hitung dasar.
a = 20
b = 6

print("\nOperasi matematika:")
print("+:", a + b)
print("-:", a - b)
print("*:", a * b)
print("/:", a / b)
print("//:", a // b)
print("%:", a % b)

# Bagian 4: akses dan manipulasi list.
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]
print("\nList buah:", buah)
print("elemen pertama:", buah[0])
print("elemen ketiga:", buah[2])

buah.append("semangka")
print("setelah append:", buah)

buah.remove("jeruk")
print("setelah remove:", buah)

terakhir = buah.pop()
print("hasil pop:", terakhir)
print("list akhir:", buah)

# Bagian 5: input dari user.
nama = input("\nMasukkan nama: ")
umur = input("Masukkan umur: ")
print(f"Halo, nama saya {nama} dan umur saya {umur} tahun.")