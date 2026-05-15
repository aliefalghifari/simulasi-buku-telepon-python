import os
from database import Database

class Telepon:
    def __init__(self):
        # Gunakan path absolute atau relative yang benar
        db_path = os.path.join(os.path.dirname(__file__), 'database.json') #memastikan path ke database.json
        self.db = Database(db_path) #menjalankan class database dengan path yang benar

    def tambah_kontak(self, nama, nomor):
        self.db.add_contact(nama, nomor)

    def lihat_kontak(self, nama):
        return self.db.get_contact(nama)
    
    def daftar_kontak(self):
        return self.db.list_contacts()

if __name__ == "__main__":
    print("Selamat datang di aplikasi telepon!")
    print("1. Panggilan")
    print("2. Tambah Kontak")
    input_user = input("Masukkan pilihan (1/2): ")
    telepon = Telepon() #membuat variabel telepon untuk mengakses class Telepon

    if input_user == '1':
        print("Siapa yang ingin anda panggil?")
        daftar_kontak = telepon.daftar_kontak() #memanggil fungsi daftar_kontak untuk memperlihatkan daftar kontak
        
        if not daftar_kontak: #jika tidak ada kontak, tampilkan pesan
            print("Tidak ada kontak yang tersedia.")
        else:
            # Tampilkan daftar kontak dengan nomor urut
            for i, nama in enumerate(daftar_kontak, 1): #menampilkan daftar kontak dengan index mulai dari 1
                print(f"{i}. {nama}")
            
            while True:
                pilihan_panggilan = input("Masukkan pilihan (1-{}): ".format(len(daftar_kontak)))
                
                # Validasi input adalah angka
                if not pilihan_panggilan.isdigit():
                    print("Pilihan harus berupa angka. Silakan coba lagi.")
                    continue
                
                pilihan_idx = int(pilihan_panggilan) - 1 #nilai index mulai dari 0, jadi kurangi 1 dari input pengguna                
                # Validasi pilihan ada di range yang benar
                if pilihan_idx < 0 or pilihan_idx >= len(daftar_kontak):
                    print(f"Pilihan harus antara 1-{len(daftar_kontak)}. Silakan coba lagi.")
                    continue
                
                # Jika valid, hubungi kontak
                nama_dipilih = daftar_kontak[pilihan_idx]
                nomor_dipilih = telepon.lihat_kontak(nama_dipilih)
                print(f"Menghubungi {nama_dipilih} di {nomor_dipilih}...")
                break
    
    elif input_user == '2':
        while True:
            nama_baru = input("Masukkan nama kontak baru: ")
            nomor_baru = input("Masukkan nomor telepon baru: ")
            
            # Validasi: nama tidak boleh kosong
            if not nama_baru:
                print("Nama tidak boleh kosong. Silakan coba lagi.")
                continue
            
            # Validasi: nomor hanya boleh integer
            if not nomor_baru.isdigit():
                print("Nomor telepon harus berisi angka saja. Silakan coba lagi.")
                continue
            
            # Jika valid, tambahkan kontak
            telepon.tambah_kontak(nama_baru, nomor_baru)
            print(f"Kontak {nama_baru} dengan nomor {nomor_baru} berhasil ditambahkan!")
            break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    