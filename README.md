# TUGAS-1-KEAMANAN-INFORMASI

# DES Constants
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 
     3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 
     10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 
     15, 12, 9, 7, 3, 10, 5, 0],
    [15, 2, 8, 14, 3, 4, 9, 7, 
     5, 6, 10, 11, 12, 0, 1, 13]
]

# Tambahkan S-box S2 hingga S8 di sini dengan cara yang sama...

PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

SHIFTS = [
    1, 1, 2, 2,
    2, 2, 1, 2,
    2, 2, 2, 2,
    1, 2, 2, 2
]

# Fungsi bantu untuk melakukan permutasi
def permute(data, perm):
    result = 0
    for i in range(len(perm)):
        result <<= 1
        result |= (data >> (64 - perm[i])) & 1
    return result

# Fungsi untuk menjadwalkan kunci
def key_schedule(key):
    # Melakukan permutasi kunci awal menggunakan PC1
    key = permute(key, PC1)
    
    # Memisahkan kunci menjadi dua bagian: kiri dan kanan
    left = (key >> 28)
    right = (key & 0x0FFFFFFF)
    
    subkeys = []
    
    for shift in SHIFTS:
        # Melakukan pergeseran pada bagian kiri dan kanan
        left = ((left << shift) | (left >> (28 - shift))) & 0x0FFFFFFF
        right = ((right << shift) | (right >> (28 - shift))) & 0x0FFFFFFF
        
        combined = (left << 28) | right
        # Menambahkan kunci yang telah dipermutasi ke dalam daftar subkunci
        subkeys.append(permute(combined, PC2))
    
    return subkeys

# Fungsi placeholder untuk enkripsi DES
def des_encrypt(data, key):
    subkeys = key_schedule(key)
    
    # Melakukan Permutasi Awal
    data = permute(data, IP)
    
    # Memisahkan data menjadi dua bagian: kiri dan kanan
    left = (data >> 32)
    right = (data & 0xFFFFFFFF)
    
    # Melakukan 16 putaran pemrosesan
    for i in range(16):
        # Fungsi putaran (F) placeholder
        pass  # Implementasikan fungsi putaran di sini

    # Menggabungkan bagian dan menerapkan permutasi akhir
    combined = (right << 32) | left
    data = permute(combined, FP)
    
    return data

# Contoh penggunaan
if __name__ == "__main__":
    # Kunci dan data contoh
    key = 0x0123456789ABCDEF
    data = 0x0123456789ABCDEF
    encrypted_data = des_encrypt(data, key)
    print(f"Data Terenkripsi: {encrypted_data:016X}")
