import numpy as np

matrix1 = np.random.randn(5, 5)

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrix1[i][j] = i+j

matrix2 = np.random.randn(5, 5)

for i in range(len(matrix2)):
    for j in range(len(matrix2[0])):
        matrix2[i][j] = 2

matrix3 = np.random.randn(5, 5)

for i in range(len(matrix3)):
    for j in range(len(matrix3[0])):
        matrix3[i][j] = 3

vector1 = [10, 10, 10, 10, 10]
vector2 = [20, 20, 20, 20, 20]
vector3 = [30, 30, 30, 30, 30]

print(matrix1)
print(matrix2)
print(matrix3)

print(vector1)
print(vector2)
print(vector3)

print("After zip")

for a,b,c in zip([matrix1,vector1],
                 [matrix2,vector2],
                 [matrix3,vector3]):

    print("a:")
    print(a)
    print("b:")
    print(b)
    print("c:")
    print(c)

print("dot ")
matrix1 += matrix1*matrix1
print(matrix1)