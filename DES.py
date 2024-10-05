import random

def generate_key():
    # Membuat 64-bit key (8 byte)
    key = ''.join([str(random.randint(0, 1)) for _ in range(64)])
    return key

def permute(block, table):
    return ''.join([block[i-1] for i in table])

def feistel_function(data, key):
    # Contoh permutasi sederhana (ubah sesuai tabel permutasi)
    e_table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 
               12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 
               20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 
               30, 31, 32, 1]
    # Expand dari 32-bit menjadi 48-bit
    expanded_data = permute(data, e_table)
    
    # XOR data yang sudah dipermutasikan dengan kunci
    xor_data = xor(expanded_data, key)
    
    # Contoh fungsi substitusi dan permutasi P, ubah sesuai kebutuhan
    # Misalnya, kita bisa mengimplementasikan S-box di sini
    return xor_data

def xor(a, b):
    return ''.join(['1' if i != j else '0' for i, j in zip(a, b)])

def des_encrypt(plain_text, key):
    # Inisialisasi permutasi (IP) tabel
    ip_table = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
    
    # Apply initial permutation
    plain_text = permute(plain_text, ip_table)
    
    # Bagi teks menjadi kiri dan kanan
    left, right = plain_text[:32], plain_text[32:]
    
    # 16 rounds Feistel structure
    for i in range(16):
        right_expanded = feistel_function(right, key) # Apply f(R, K)
        new_right = xor(left, right_expanded)  # XOR with left part
        left = right
        right = new_right
    
    # Setelah 16 putaran, gabungkan kembali kiri dan kanan
    final_text = right + left
    
    # Final Permutation (FP)
    fp_table = [40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25]
    
    # Apply final permutation
    cipher_text = permute(final_text, fp_table)
    
    return cipher_text

def des_decrypt(cipher_text, key):
    # Sama seperti enkripsi, namun urutan key dibalik
    return des_encrypt(cipher_text, key)

if __name__ == "__main__":
    key = generate_key()
    print(f"Generated Key: {key}")
    
    plain_text = "1010101111001101111001101111001101001110111100011101100111100001"  # Contoh plain text (64-bit)
    
    cipher_text = des_encrypt(plain_text, key)
    print(f"Cipher Text: {cipher_text}")
    
    decrypted_text = des_decrypt(cipher_text, key)
    print(f"Decrypted Text: {decrypted_text}")
    
    # Verifikasi hasil
    assert plain_text == decrypted_text, "Dekripsi gagal!"
    print("Dekripsi sukses!")
