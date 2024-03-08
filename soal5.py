def even_square_numbers(n):
    # Menggunakan list comprehension untuk menghasilkan list bilangan kuadrat dari bilangan genap antara 1 hingga n
    return [x**2 for x in range(2, n+1, 2)]

# Panggil fungsi even_square_numbers dengan nilai n tertentu
n = 100
result = even_square_numbers(n)

# Menampilkan hasil
print("List bilangan kuadrat dari bilangan genap antara 1 hingga", n, "adalah:")
print(result)
