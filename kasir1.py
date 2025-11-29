# Hati-hati dengan tanda kurung tutupnya, harus ada 2 di akhir ))
# Satu tutup punya int(, satu lagi punya input(

nama_barang = input("Masukkan nama barang: ")

harga = int(input("Masukkan harga satuan: "))

jumlah = int(input("Masukkan jumlah beli: "))

# Hitung
total = harga * jumlah

# Tampilkan
print("Barang:", nama_barang)
print("Total Bayar:", total)