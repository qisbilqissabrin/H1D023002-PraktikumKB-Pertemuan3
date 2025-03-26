# Program Sederhana: Sistem Pengelolaan Tugas

import random  # Library untuk menghasilkan angka acak
from datetime import datetime  # Library untuk bekerja dengan tanggal dan waktu

# Struktur Data: List untuk menyimpan tugas
list_tugas = []

# Fungsi untuk menambahkan tugas
def tambah_tugas(nama, deadline):
    tugas = {
        'nama': nama,
        'deadline': deadline,
        'prioritas': random.choice(['Tinggi', 'Sedang', 'Rendah'])
    }
    list_tugas.append(tugas)
    print(f"Tugas '{nama}' berhasil ditambahkan!")

# Fungsi untuk menampilkan semua tugas
def tampilkan_tugas():
    if not list_tugas:
        print("Belum ada tugas yang terdaftar.")
        return

    print("\nDaftar Tugas:")
    for idx, tugas in enumerate(list_tugas, start=1):
        print(f"{idx}. {tugas['nama']} - Deadline: {tugas['deadline']} - Prioritas: {tugas['prioritas']}")

# Fungsi untuk menghapus tugas berdasarkan indeks
def hapus_tugas(index):
    if 0 <= index < len(list_tugas):
        tugas = list_tugas.pop(index)
        print(f"Tugas '{tugas['nama']}' berhasil dihapus!")
    else:
        print("Indeks tidak valid.")

# Program utama
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Tampilkan Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            nama = input("Masukkan nama tugas: ")
            deadline = input("Masukkan deadline (YYYY-MM-DD): ")
            try:
                datetime.strptime(deadline, "%Y-%m-%d")  # Validasi format tanggal
                tambah_tugas(nama, deadline)
            except ValueError:
                print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")

        elif pilihan == '2':
            tampilkan_tugas()

        elif pilihan == '3':
            tampilkan_tugas()
            try:
                index = int(input("Masukkan nomor tugas yang akan dihapus: ")) - 1
                hapus_tugas(index)
            except ValueError:
                print("Masukkan nomor yang valid.")

        elif pilihan == '4':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
