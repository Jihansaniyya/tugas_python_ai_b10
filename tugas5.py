# Kumpulan function dasar.
def greet(nama: str) -> str:
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    return a + b


def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


# Class student sederhana untuk simpan data dan nilai.
class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] | None = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float) -> None:
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self) -> str:
        return (
            f"Student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai()}, status={self.status()})"
        )


if __name__ == "__main__":
    # Demo function.
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print("tambah(5, 7):", tambah(5, 7))
    print("tambah(10):", tambah(10))
    print("rata_rata([80, 90, 100]):", rata_rata([80, 90, 100]))
    print("rata_rata([]):", rata_rata([]))

    # Demo class Student.
    print("\n=== CLASS STUDENT ===")
    mhs1 = Student("Jihan", "230011001")
    mhs1.tambah_nilai(80)
    mhs1.tambah_nilai(85)
    mhs1.tambah_nilai(90)

    mhs2 = Student("Saniyya", "230011002")
    mhs2.tambah_nilai(60)
    mhs2.tambah_nilai(70)
    mhs2.tambah_nilai(65)

    print(mhs1)
    print("rata-rata:", mhs1.rata_nilai())
    print("status:", mhs1.status())

    print(mhs2)
    print("rata-rata:", mhs2.rata_nilai())
    print("status:", mhs2.status())
