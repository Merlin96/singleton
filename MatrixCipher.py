def cipher(source=None,key=None):
    source=

lookup_table = {'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5,
                'Е': 6, 'Ж': 7, 'З': 8, 'И': 9, 'Й': 10,
                'К': 11, 'Л': 12, 'М': 13, 'Н': 14, 'О': 15,
                'П': 16, 'Р': 17, 'С': 18, 'Т': 19, 'У': 20,
                'Ф': 21, 'Х': 22, 'Ц': 23, 'Ч': 24, 'Ш': 25, 'Щ': 26
                'Ъ': 28,'Ы': 29, 'Ь': 30, 'Э': 31, 'Ю': 32, 'Я': 33}

m = int(input("Row: "))
n = int(input("Column: "))
print("Creating Matrix...")
f_matrix = []
for i in range(m):
    matrix = []
    for j in range(n):
        matrix.append(int(input("Enter num: ")))
    f_matrix.append(matrix)

for i in range(m):
    for j in range(n):
        print(f_matrix[i][j], end=" ")
    print()
