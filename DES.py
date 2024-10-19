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

S2 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 
     3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 
     10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 
     15, 12, 9, 7, 3, 10, 5, 0],
    [15, 2, 8, 14, 3, 4, 9, 7, 
     5, 6, 10, 11, 12, 0, 1, 13]
]

S3 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 
     3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 
     10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 
     15, 12, 9, 7, 3, 10, 5, 0],
    [15, 2, 8, 14, 3, 4, 9, 7, 
     5, 6, 10, 11, 12, 0, 1, 13]
]

S4 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 
     3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 
     10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 
     15, 12, 9, 7, 3, 10, 5, 0],
    [15, 2, 8, 14, 3, 4, 9, 7, 
     5, 6, 10, 11, 12, 0, 1, 13]
]

S5 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 
     3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 
     10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 
     15, 12, 9, 7, 3, 10, 5, 0],
    [15, 2, 8, 14, 3, 4, 9, 7, 
     5, 6, 10, 11, 12, 0, 1, 13]
]

S6 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 
     3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 
     10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 
     15, 12, 9, 7, 3, 10, 5, 0],
    [15, 2, 8, 14, 3, 4, 9, 7, 
     5, 6, 10, 11, 12, 0, 1, 13]
]

S7 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 
     3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 
     10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 
     15, 12, 9, 7, 3, 10, 5, 0],
    [15, 2, 8, 14, 3, 4, 9, 7, 
     5, 6, 10, 11, 12, 0, 1, 13]
]

S8 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 
     3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 
     10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 
     15, 12, 9, 7, 3, 10, 5, 0],
    [15, 2, 8, 14, 3, 4, 9, 7, 
     5, 6, 10, 11, 12, 0, 1, 13]
]

# P-table for permutation after S-boxes
P = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

# Expansion table (E) to expand 32-bit right half to 48 bits
E = [
    32, 1, 2, 3, 4, 5, 4, 5,
    6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32, 1
]

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

# Helper function to expand 32-bit data to 48 bits using E-table
def expand(data):
    return permute(data, E)

# Helper function to apply S-boxes
def sbox(data):
    output = 0
    for i in range(8):
        block = (data >> (42 - 6 * i)) & 0x3F  # Extract 6 bits for current S-box
        row = ((block >> 4) & 0x2) | (block & 0x1)  # First and last bit for row
        col = (block >> 1) & 0xF  # Middle four bits for column
        # Select the value from S-box and append it to the result
        s_value = S1[row][col]  # Use S1 as an example, but repeat for S2 to S8
        output = (output << 4) | s_value
    return output

# Feistel F-function
def f_function(right, subkey):
    # Step 1: Expand the right half from 32 bits to 48 bits
    expanded_right = expand(right)
    
    # Step 2: XOR the expanded right half with the subkey
    xor_result = expanded_right ^ subkey
    
    # Step 3: Apply S-box substitution (8 groups of 6 bits to 4 bits)
    sbox_result = sbox(xor_result)
    
    # Step 4: Apply P-table permutation to the S-box result
    return permute(sbox_result, P)

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

# Updated DES encryption function with Feistel rounds
def des_encrypt(data, key):
    subkeys = key_schedule(key)
    
    # Perform Initial Permutation (IP)
    data = permute(data, IP)
    
    # Split data into left and right halves
    left = (data >> 32) & 0xFFFFFFFF
    right = data & 0xFFFFFFFF
    
    # 16 rounds of processing
    for i in range(16):
        # Save the old right half for swapping
        old_right = right
        
        # Feistel function: f_function(right, subkeys[i])
        right = left ^ f_function(right, subkeys[i])
        
        # Left becomes the old right half
        left = old_right
    
    # Combine left and right halves (swap back after last round)
    combined = (right << 32) | left
    
    # Apply Final Permutation (FP)
    data = permute(combined, FP)
    
    return data

# Contoh penggunaan
if __name__ == "__main__":
    # Kunci dan data contoh
    key = 0x0123456789ABCDEF
    data = 0x0123456789ABCDEF
    encrypted_data = des_encrypt(data, key)
    print(f"Data Terenkripsi: {encrypted_data:016X}")
