# Variabel global untuk menyimpan data mahasiswa
mahasiswa_list = []

# Fungsi untuk menambahkan nama mahasiswa
def create_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    mahasiswa_list.append(nama)
    print(f"{nama} telah ditambahkan.")

# Fungsi untuk menampilkan semua data mahasiswa
def read_mahasiswa():
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.")
    else:
        print("Daftar Mahasiswa:")
        for index, nama in enumerate(mahasiswa_list):
            print(f"{index + 1}. {nama}")

# Fungsi untuk mengubah nama mahasiswa berdasarkan indeks
def update_mahasiswa():
    read_mahasiswa()
    index = int(input("Masukkan nomor mahasiswa yang ingin diubah: ")) - 1
    if 0 <= index < len(mahasiswa_list):
        nama_baru = input("Masukkan nama baru: ")
        mahasiswa_list[index] = nama_baru
        print("Nama mahasiswa telah diubah.")
    else:
        print("Indeks tidak valid.")

# Fungsi untuk menghapus nama mahasiswa berdasarkan indeks
def delete_mahasiswa():
    read_mahasiswa()
    index = int(input("Masukkan nomor mahasiswa yang ingin dihapus: ")) - 1
    if 0 <= index < len(mahasiswa_list):
        deleted_name = mahasiswa_list.pop(index)
        print(f"{deleted_name} telah dihapus.")
    else:
        print("Indeks tidak valid.")

# Fungsi untuk menampilkan menu
def menu():
    print("\nMenu:")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Mahasiswa")
    print("3. Ubah Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")

# Main loop
def main():
    while True:
        menu()
        choice = input("Pilih opsi (1-5): ")
        if choice == '1':
            create_mahasiswa()
        elif choice == '2':
            read_mahasiswa()
        elif choice == '3':
            update_mahasiswa()
        elif choice == '4':
            delete_mahasiswa()
        elif choice == '5':
            print("Keluar dari program.")
            exit()
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()