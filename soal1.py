import numpy as np

def find_average(numbers):
    if numbers.size == 0:  # Periksa apakah panjang array adalah nol
        return 0
    return np.mean(numbers)

# Generate a list of random numbers
random_numbers = np.random.randint(1, 100, size=10)

# Calculate the average
average = find_average(random_numbers)

print("List angka acak:", random_numbers)
print("Rata-rata:", average)
