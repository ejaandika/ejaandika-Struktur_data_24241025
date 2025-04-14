# Meminta input jumlah deret Fibonacci
jumlah_deret = int(input("Masukkan jumlah deret Fibonacci: "))

# Inisialisasi dua angka pertama dalam deret Fibonacci
a, b = 0, 1

print("Deret Fibonacci:")
for i in range(jumlah_deret):
    print(a, end=' ')
    # Menghitung angka Fibonacci berikutnya
    a, b = b, a + b