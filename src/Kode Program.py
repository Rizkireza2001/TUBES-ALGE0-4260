import numpy as np

def input_matrix(order):
    print(f"Masukkan nilai matriks {order}:")
    matrix = []
    for i in range(order):
        row = []
        for j in range(order):
            value = float(input(f"Masukkan nilai a{i + 1}{j + 1}: "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)

def print_matrix(matrix):
    for row in matrix:
        print(row)

def menu():
    print("MENU")
    print("1. Penjumlahan dan Pengurangan Matriks")
    print("2. Matriks Transpose")
    print("3. Matriks Balikan")
    print("4. Determinan")
    print("5. Sistem Persamaan Linier")
    print("6. Keluar")

def matrix_operations_menu():
    print("PILIHAN")
    print("1. Penjumlahan matriks")
    print("2. Pengurangan matriks")

def transpose_menu():
    print("PILIHAN")
    print("1. Matriks 2x2")
    print("2. Matriks 3x3")

def determinant_menu():
    print("PILIHAN")
    print("1. Matriks 2x2")
    print("2. Matriks 3x3")

def matrix_inverse(matrix):
    det = np.linalg.det(matrix)
    if det == 0:
        return None  # Matriks tidak memiliki invers karena determinannya nol
    else:
        return np.linalg.inv(matrix)

def linear_system_solution_menu():
    print("Masukkan koefisien matriks A dan vektor b:")
    A = input_matrix(2)
    b = input_matrix(2)
    return A, b

while True:
    menu()
    choice = input("Pilih menu (1-6): ")

    if choice == '1':
        matrix_operations_menu()
        operation_choice = input("Pilih operasi (1-2): ")

        if operation_choice == '1':
            A = input_matrix(2)
            B = input_matrix(2)
            result = A + B
        elif operation_choice == '2':
            A = input_matrix(2)
            B = input_matrix(2)
            result = A - B
        else:
            print("Pilihan tidak valid")

        print("Hasil:")
        print_matrix(result)

    elif choice == '2':
        transpose_menu()
        transpose_choice = input("Pilih operasi (1-2): ")

        if transpose_choice == '1':
            A = input_matrix(2)
            result = np.transpose(A)
        elif transpose_choice == '2':
            A = input_matrix(3)
            result = np.transpose(A)
        else:
            print("Pilihan tidak valid")

        print("Hasil:")
        print_matrix(result)

    elif choice == '3':
        A = input_matrix(2)
        result = matrix_inverse(A)

        if result is not None:
            print("Hasil:")
            print_matrix(result)
        else:
            print("Matriks tidak memiliki invers.")

    elif choice == '4':
        determinant_menu()
        determinant_choice = input("Pilih operasi (1-2): ")

        if determinant_choice == '1':
            A = input_matrix(2)
            result = np.linalg.det(A)
        elif determinant_choice == '2':
            A = input_matrix(3)
            result = np.linalg.det(A)
        else:
            print("Pilihan tidak valid")

        print(f"Hasil determinan: {result}")

    elif choice == '5':
        A, b = linear_system_solution_menu()
        try:
            result = np.linalg.solve(A, b)
            print("Hasil:")
            print_matrix(result)
        except np.linalg.LinAlgError:
            print("Sistem persamaan linier tidak memiliki solusi unik.")

    elif choice == '6':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-6.")
