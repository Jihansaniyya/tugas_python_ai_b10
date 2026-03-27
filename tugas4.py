# Bagian 1: list campuran, akses elemen, slicing, dan manipulasi.
data = ["apel", 10, 3.14, "jeruk", 42, "mangga"]
print("1) List")
print("awal:", data)
print("pertama:", data[0])
print("terakhir:", data[-1])
print("slicing [1:6:2]:", data[1:6:2])

print("\nappend")
print("sebelum:", data)
data.append("anggur")
print("sesudah:", data)

print("\ninsert")
print("sebelum:", data)
data.insert(2, "pisang")
print("sesudah:", data)

print("\nextend")
print("sebelum:", data)
data.extend([100, "melon"])
print("sesudah:", data)

print("\npop")
print("sebelum:", data)
hasil_pop = data.pop()
print("yang di-pop:", hasil_pop)
print("sesudah:", data)

print("\nremove")
print("sebelum:", data)
data.remove("jeruk")
print("sesudah:", data)

# Bagian 2: tuple tidak bisa diubah langsung, plus contoh unpacking.
info = ("Andi", 21, "Informatika", 2024, "Bandung")
print("\n2) Tuple")
print("tuple:", info)
print("len:", len(info))
print("index 0:", info[0])
print("index 3:", info[3])

nama, umur, *sisanya = info
print("unpacking ->", nama, umur, sisanya)

# Bagian 3: operasi himpunan pada dua set dengan elemen tumpang tindih.
a = {1, 2, 3, 4, 4, 5}
b = {4, 5, 6, 7, 7}
print("\n3) Set")
print("set a:", a)
print("set b:", b)
print("union:", a | b)
print("intersection:", a & b)
print("difference a-b:", a - b)
print("sym diff:", a ^ b)

# Bagian 4: operasi dasar dictionary (tambah, ubah, hapus, lalu iterasi).
mahasiswa = {
    "nama": "Jihan",
    "nim": "230011001",
    "angkatan": 2023,
    "kota": "Semarang",
}
print("\n4) Dictionary")
print("awal:", mahasiswa)

mahasiswa["jurusan"] = "Teknik Informatika"
mahasiswa["kota"] = "Sleman"
del mahasiswa["angkatan"]

print("setelah ubah data:", mahasiswa)
print("keys:", mahasiswa.keys())
print("values:", mahasiswa.values())
print("items:", mahasiswa.items())

for k, v in mahasiswa.items():
    print(f"{k}: {v}")

# Bagian 5: nested structure berupa list yang berisi dictionary buku.
daftar_buku = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005},
    {"judul": "Bumi", "penulis": "Tere Liye", "tahun": 2014},
    {"judul": "Negeri 5 Menara", "penulis": "Ahmad Fuadi", "tahun": 2009},
    {"judul": "Pulang", "penulis": "Leila S. Chudori", "tahun": 2012},
]

print("\n5) Nested structure")
print("judul buku:")
for buku in daftar_buku:
    print("-", buku["judul"])

batas_tahun = 2010
hasil_filter = [b for b in daftar_buku if b["tahun"] >= batas_tahun]
print(f"buku tahun >= {batas_tahun}:", hasil_filter)

# Bagian 6: contoh list/dict/set comprehension.
angka = list(range(1, 21))
genap = [n for n in angka if n % 2 == 0]
kuadrat = [n**2 for n in angka]

print("\n6) Comprehension")
print("genap 1-20:", genap)
print("kuadrat 1-20:", kuadrat)

status_angka = {n: "genap" if n % 2 == 0 else "ganjil" for n in range(1, 11)}
print("dict 1-10:", status_angka)

kalimat = "Python Data Structures"
huruf_unik = {h.lower() for h in kalimat if h.isalpha()}
print("huruf unik:", huruf_unik)

# Bagian 7: cek keanggotaan dan posisi item secara ringkas.
print("\n7) Cek keanggotaan")
cek_list = "apel"
cek_set = 6

if cek_list in data:
    print(f"'{cek_list}' ada di list, index {data.index(cek_list)}")
else:
    print(f"'{cek_list}' tidak ada di list")

if cek_set in b:
    print(f"{cek_set} ada di set b")
else:
    print(f"{cek_set} tidak ada di set b")
