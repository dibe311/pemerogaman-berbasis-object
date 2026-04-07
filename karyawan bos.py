class Karyawan:
    # Memiliki atribut nik, nama, dan jabatan 
    def __init__(self, nik, nama, jabatan):
        self.nik = nik
        self.nama = nama
        self.jabatan = jabatan

    def __str__(self):
        # Format string untuk memudahkan tampilan dalam bentuk tabel
        return f"| {self.nik:<10} | {self.nama:<20} | {self.jabatan:<15} |"


class SistemKaryawan:
    def __init__(self):
        # Memiliki atribut list database_karyawan 
        self.database_karyawan = []

    # Method mencari karyawan berdasarkan NIK [cite: 10]
    def cari_karyawan(self, nik):
        for karyawan in self.database_karyawan:
            if karyawan.nik == nik:
                return karyawan
        return None

    # Method menambah objek ke list dan memastikan NIK tidak duplikat [cite: 9]
    def tambah_karyawan(self, karyawan_baru):
        if self.cari_karyawan(karyawan_baru.nik):
            print("❌ NIK sudah terdaftar! Penambahan dibatalkan.")
        else:
            self.database_karyawan.append(karyawan_baru)
            print("✅ Karyawan berhasil ditambahkan!")

    # Method menampilkan daftar karyawan dalam bentuk tabel sederhana 
    def tampilkan_semua(self):
        if not self.database_karyawan:
            print("Data karyawan masih kosong.")
            return
        
        print("-" * 55)
        print(f"| {'NIK':<10} | {'Nama':<20} | {'Jabatan':<15} |")
        print("-" * 55)
        for karyawan in self.database_karyawan:
            print(karyawan)
        print("-" * 55)


# Implementasi Menu Output Program 
def main():
    sistem = SistemKaryawan()

    while True:
        print("\n1. Tambah Karyawan")
        print("2. Cari Karyawan (NIK)")
        print("3. Lihat Semua")
        print("4. Keluar")
        
        pilihan = input("Pilihan: ")

        if pilihan == '1':
            print()
            nik = input("Masukkan NIK: ")
            nama = input("Masukkan Nama: ")
            jabatan = input("Masukkan Jabatan: ")
            
            karyawan = Karyawan(nik, nama, jabatan)
            sistem.tambah_karyawan(karyawan)
            
        elif pilihan == '2':
            print()
            nik = input("Masukkan NIK yang dicari: ")
            karyawan = sistem.cari_karyawan(nik)
            
            if karyawan:
                print("\nData Ditemukan:")
                print("-" * 55)
                print(f"| {'NIK':<10} | {'Nama':<20} | {'Jabatan':<15} |")
                print("-" * 55)
                print(karyawan)
                print("-" * 55)
            else:
                print("❌ Karyawan dengan NIK tersebut tidak ditemukan.")
                
        elif pilihan == '3':
            print("\nDaftar Karyawan:")
            sistem.tampilkan_semua()
            
        elif pilihan == '4':
            print("Keluar dari program. Terima kasih!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Menjalankan program utama
if __name__ == "__main__":
    main()
