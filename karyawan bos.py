import json
import os

class Karyawan:
    def __init__(self, nik, nama, jabatan):
        self.nik = nik
        self.nama = nama
        self.jabatan = jabatan

    def __str__(self):
        return f"| {self.nik:<10} | {self.nama:<20} | {self.jabatan:<15} |"

    # Method baru untuk mengubah objek menjadi dictionary agar bisa disimpan ke JSON
    def to_dict(self):
        return {
            "nik": self.nik,
            "nama": self.nama,
            "jabatan": self.jabatan
        }


class SistemKaryawan:
    def __init__(self):
        self.database_karyawan = []
        self.nama_file = "database_karyawan.json" # Nama file database JSON
        self.muat_data() # Otomatis memuat data saat program dijalankan

    # Method baru: Memuat data dari JSON ke dalam list of objects
    def muat_data(self):
        try:
            with open(self.nama_file, 'r') as file:
                data_json = json.load(file)
                for item in data_json:
                    # Mengubah kembali dictionary dari JSON menjadi objek Karyawan
                    karyawan = Karyawan(item['nik'], item['nama'], item['jabatan'])
                    self.database_karyawan.append(karyawan)
        except FileNotFoundError:
            # Jika file belum ada (baru pertama kali jalan), tidak masalah
            pass
        except json.JSONDecodeError:
            # Jika file ada tapi kosong atau isinya error
            print("Peringatan: File JSON kosong atau rusak.")

    # Method baru: Menyimpan data dari list of objects ke JSON
    def simpan_data(self):
        with open(self.nama_file, 'w') as file:
            # Mengubah list of objects menjadi list of dictionaries
            data_json = [karyawan.to_dict() for karyawan in self.database_karyawan]
            # Menulis ke file json dengan indentasi agar rapi dan mudah dibaca
            json.dump(data_json, file, indent=4)

    def cari_karyawan(self, nik):
        for karyawan in self.database_karyawan:
            if karyawan.nik == nik:
                return karyawan
        return None

    def tambah_karyawan(self, karyawan_baru):
        if self.cari_karyawan(karyawan_baru.nik):
            print("❌ NIK sudah terdaftar! Penambahan dibatalkan.")
        else:
            self.database_karyawan.append(karyawan_baru)
            self.simpan_data() # Panggil method simpan_data setelah update list
            print("✅ Karyawan berhasil ditambahkan dan disimpan ke database!")

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

if __name__ == "__main__":
    main()
