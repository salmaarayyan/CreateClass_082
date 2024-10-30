class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def luas(self):
        return self.panjang * self.lebar

    def str(self):
        return f"Persegi panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"


def main():
    print("=== Program Persegi Panjang ===")
    try:
        panjang = float(input("Masukkan panjang persegi panjang (cm): "))
        lebar = float(input("Masukkan lebar persegi panjang (cm): "))
        
        if panjang <= 0 or lebar <= 0:
            print("Panjang dan lebar harus bernilai positif!")
            return

        persegi_panjang = PersegiPanjang(panjang, lebar)
        
        print("\n=== Hasil Perhitungan ===")
        print(persegi_panjang)
        print("Keliling:", persegi_panjang.keliling(), "cm")
        print("Luas:", persegi_panjang.luas(), "cm²")
        
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

main()