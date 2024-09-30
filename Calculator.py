def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Tidak bisa membagi dengan nol!"
    return x / y

def kalkulator():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    while True:
        pilihan = input("Masukkan pilihan (1/2/3/4) atau 'q' untuk keluar: ")

        if pilihan == 'q':
            print("Terima kasih telah menggunakan kalkulator!")
            break
        
        if pilihan in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Masukkan angka pertama: "))
                num2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
                continue

            if pilihan == '1':
                print(f"Hasil: {tambah(num1, num2)}")
            elif pilihan == '2':
                print(f"Hasil: {kurang(num1, num2)}")
            elif pilihan == '3':
                print(f"Hasil: {kali(num1, num2)}")
            elif pilihan == '4':
                print(f"Hasil: {bagi(num1, num2)}")
        else:
            print("Pilihan tidak valid! Harap pilih 1, 2, 3, atau 4.")

# Memulai kalkulator
kalkulator()
