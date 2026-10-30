import array

# 1 
# Aturan Kelulusan:

# Jika nilai lebih besar atau sama dengan 75, statusnya: "Lulus".

# Jika nilai di bawah 75, statusnya: "Tidak Lulus".

score = 75

# code here---------------
# if score >= 75:
#   print('Lulus')
# else:
#   print('Tidak Lulus')
# -------------------------

# 2
# Aturan Nilai Huruf:

# Nilai 85 - 100: Huruf "A"

# Nilai 70 - 84: Huruf "B"

# Nilai 55 - 69: Huruf "C"

# Nilai 40 - 54: Huruf "D"

# Nilai di bawah 40: Huruf "E"

# code here---------------
# if score >= 85:
#   print('A')
# elif score >= 70:
#   print('B')
# elif score >= 55:
#   print('C')
# elif score >= 40:
#   print('D')
# else:
#   print('E')
# -------------------------

# 3
# Validasi Input:

# Jika pengguna memasukkan angka di luar rentang 0 sampai 100, cetak pesan error: "Nilai tidak valid! Masukkan angka antara 0 sampai 100."

# code here---------------
# number = int(input('Enter number(0-100): '))

# if number < 0 or number > 100:
#   print("Nilai tidak valid! Masukkan angka antara 0 sampai 100.")
# else:
#   print(f'your number is {number}')
# -------------------------


arrayVariable = array.array('i', [1, 2, 3, 4, 5, 6, 7, 'hello'])
print(arrayVariable)