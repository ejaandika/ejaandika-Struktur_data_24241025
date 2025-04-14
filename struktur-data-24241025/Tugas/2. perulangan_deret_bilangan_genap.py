# Meminta input jumlah deret dari pengguna
jumlah_deret = int(input("Masukkan jumlah deret bilangan genap: \10"))

# Inisialisasi variabel untuk menyimpan bilangan genap
bilangan_genap = []

# Menggunakan perulangan untuk menghasilkan deret bilangan genap
for i in range(jumlah_deret):
    bilangan_genap.append(i * 2)

# Menampilkan deret bilangan genap
print("Deret bilangan genap:", bilangan_genap)
