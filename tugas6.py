import numpy as np
import pandas as pd
import os

# Seed dipakai biar hasil angka acak tetap konsisten.
np.random.seed(42)


class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        if total == 0:
            return 0.0
        lulus = (self.df["nilai"] >= threshold).sum()
        return float((lulus / total) * 100)

    def save_summary(self, path: str) -> None:
        total = len(self.df)
        lulus = int((self.df["status"] == "LULUS").sum())
        tidak_lulus = int((self.df["status"] == "TIDAK LULUS").sum())

        with open(path, "a", encoding="utf-8") as f:
            f.write("\n=== RINGKASAN OOP GRADEBOOK ===\n")
            f.write(f"Jumlah data        : {total}\n")
            f.write(f"Rata-rata nilai    : {self.average():.2f}\n")
            f.write(f"Persentase lulus   : {self.pass_rate():.2f}%\n")
            f.write(f"Jumlah lulus       : {lulus}\n")
            f.write(f"Jumlah tidak lulus : {tidak_lulus}\n")

    def __str__(self) -> str:
        return f"GradeBook(total_data={len(self.df)}, rata_rata={self.average():.2f})"


if __name__ == "__main__":
    # Bagian NumPy: buat data nilai dan hitung statistik dasar.
    nilai_ujian = np.random.randint(55, 101, size=10)

    rata = np.mean(nilai_ujian)
    median = np.median(nilai_ujian)
    std = np.std(nilai_ujian)
    minimum = np.min(nilai_ujian)
    maksimum = np.max(nilai_ujian)

    print("=== NUMPY ===")
    print("Nilai ujian:", nilai_ujian)
    print(f"Rata-rata   : {rata:.2f}")
    print(f"Median      : {median:.2f}")
    print(f"Std deviasi : {std:.2f}")
    print(f"Min         : {minimum}")
    print(f"Max         : {maksimum}")

    # Bagian pandas: buat DataFrame mahasiswa dan status kelulusan.
    data = {
        "nama": ["Budi", "Sinta", "Raka", "Dina", "Arif", "Nadia"],
        "nim": ["A001", "A002", "A003", "A004", "A005", "A006"],
        "nilai": nilai_ujian[:6],
    }
    df = pd.DataFrame(data)
    df["status"] = np.where(df["nilai"] >= 70, "LULUS", "TIDAK LULUS")

    print("\n=== PANDAS ===")
    print(df.head())

    total_baris = len(df)
    total_lulus = int((df["status"] == "LULUS").sum())
    total_tidak_lulus = int((df["status"] == "TIDAK LULUS").sum())

    # Bagian file I/O: tulis ringkasan statistik dan DataFrame ke txt.
    path_ringkasan = os.path.join(os.getcwd(), "ringkasan_tugas6.txt")
    with open(path_ringkasan, "w", encoding="utf-8") as f:
        f.write("=== RINGKASAN NUMPY ===\n")
        f.write(f"Nilai ujian         : {nilai_ujian.tolist()}\n")
        f.write(f"Rata-rata           : {rata:.2f}\n")
        f.write(f"Median              : {median:.2f}\n")
        f.write(f"Standar deviasi     : {std:.2f}\n")
        f.write(f"Nilai minimum       : {minimum}\n")
        f.write(f"Nilai maksimum      : {maksimum}\n")

        f.write("\n=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah baris        : {total_baris}\n")
        f.write(f"Jumlah lulus        : {total_lulus}\n")
        f.write(f"Jumlah tidak lulus  : {total_tidak_lulus}\n")

    # Bagian OOP: pakai class GradeBook dan simpan ringkasan tambahannya.
    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print(f"Average    : {gb.average():.2f}")
    print(f"Pass rate  : {gb.pass_rate():.2f}%")
    gb.save_summary(path_ringkasan)
    print(f"Ringkasan tersimpan di: {path_ringkasan}")
