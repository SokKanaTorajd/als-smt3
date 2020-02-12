""" Tugas Numpy """

import numpy as np

"""soal 1 - input 2 matrix 3x3"""

list_matrix = []

for i in range(2):
    b = int(input("masukkan jumlah baris:"))
    k = int(input("masukkan jumlah kolom:"))
    nilai = list(map(int, input("masukkan nilai, pisahkan dengan spasi:").split()))
    print()
    m = np.array(nilai).reshape(b,k)
    list_matrix.append(m)

print(list_matrix)

"""soal 2 - perkalian matrix dengan numpy"""

perkalian = list_matrix[0].dot(list_matrix[1])
print("perkalian matrix\n", perkalian)

"""soal 3 - pembagian matrix dengan numpy"""

pembagian = np.divide(list_matrix[1],list_matrix[0])
print("pembagian matrix\n", pembagian)
