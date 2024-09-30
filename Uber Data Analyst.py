import pandas as pd

def load_data(file_path):
    """Muat data dari file CSV."""
    try:
        data = pd.read_csv(file_path)
        print("Data berhasil dimuat!")
        return data
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan path sudah benar.")
        return None
    except OSError as e:
        print(f"Terjadi kesalahan saat memuat file: {e}")
        return None

def analisis_data(data):
    """Melakukan analisis dasar pada data."""
    print("\nStatistik Deskriptif:")
    print(data.describe())
    
    print("\nJumlah perjalanan per tanggal:")
    print(data['Date'].value_counts())
    
    print("\nJumlah pelanggan unik:")
    print(data['Customer'].nunique())

def main():
    file_path = input("Masukkan path file CSV: ").strip('"')  # Menghapus tanda kutip jika ada
    data = load_data(file_path)
    
    if data is not None:
        # Pastikan kolom yang ada sesuai dengan data Anda
        if 'Date' in data.columns and 'Customer' in data.columns:
            analisis_data(data)
        else:
            print("Kolom 'Date' atau 'Customer' tidak ditemukan dalam data.")

if __name__ == "__main__":
    main()
