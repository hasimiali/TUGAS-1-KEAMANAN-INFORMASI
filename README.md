# TUGAS-1-KEAMANAN-INFORMASI DES (Data Encryption Standard) Implementation

Implementasi algoritma Data Encryption Standard (DES) dalam Python. DES adalah algoritma enkripsi simetris yang digunakan untuk mengamankan data dengan menggunakan kunci rahasia.

## Deskripsi Program

Program ini mencakup fungsi-fungsi untuk enkripsi menggunakan algoritma DES, termasuk:
- Permutasi awal dan akhir
- Tabel S-box untuk substitusi
- Proses pengaturan kunci untuk menghasilkan subkunci

### Konstanta DES

Program mendefinisikan semua konstanta yang diperlukan untuk algoritma DES, seperti:
- Permutasi awal (`IP`)
- Permutasi akhir (`FP`)
- S-box (`S1` hingga `S8`)
- Tabel kunci (`PC1` dan `PC2`)
- Array pergeseran (`SHIFTS`)

### Fungsi Utama

- `permute(data, perm)`: Melakukan permutasi pada data sesuai dengan array permutasi yang diberikan.
- `key_schedule(key)`: Menghasilkan 16 subkunci yang digunakan selama proses enkripsi.
- `des_encrypt(data, key)`: Melakukan proses enkripsi DES pada data menggunakan kunci yang diberikan.

### Contoh Penggunaan

```python
if __name__ == "__main__":
    # Kunci dan data contoh
    key = 0x0123456789ABCDEF
    data = 0x0123456789ABCDEF
    encrypted_data = des_encrypt(data, key)
    print(f"Data Terenkripsi: {encrypted_data:016X}")
