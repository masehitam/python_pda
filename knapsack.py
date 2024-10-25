def knapsack_bruteforce(values, weights, capacity):
    n = len(values)
    max_value = 0
    best_combination = []

    # Cek semua kemungkinan kombinasi (2^n kemungkinan)
    for i in range(2**n):
        total_value = 0
        total_weight = 0
        combination = []

        # 1.	(0, 0, 0): Tidak ada item yang diambil. Nilai = 0, Bobot = 0.
        # 2.	(0, 0, 1): Hanya item 3 yang diambil. Nilai = 120, Bobot = 30.
        # 3.	(0, 1, 0): Hanya item 2 yang diambil. Nilai = 100, Bobot = 20.
        # 4.	(0, 1, 1): Item 2 dan 3 yang diambil. Nilai = 100 + 120 = 220, Bobot = 20 + 30 = 50.
        # 5.	(1, 0, 0): Hanya item 1 yang diambil. Nilai = 60, Bobot = 10.
        # 6.	(1, 0, 1): Item 1 dan 3 yang diambil. Nilai = 60 + 120 = 180, Bobot = 10 + 30 = 40.
        # 7.	(1, 1, 0): Item 1 dan 2 yang diambil. Nilai = 60 + 100 = 160, Bobot = 10 + 20 = 30.
        # 8.	(1, 1, 1): Semua item diambil. Nilai = 60 + 100 + 120 = 280, Bobot = 10 + 20 + 30 = 60 (tidak valid karena melebihi kapasitas tas).
        # Cek setiap item apakah dipilih atau tidak
        for j in range(n):
            # J = 0 , 1 , 2
            # 1 << j = 1 , 2 , 4
            if i & (1 << j):  # Jika bit ke-j dalam angka i adalah 1, berarti item ke-j dipilih
                total_value += values[j]
                total_weight += weights[j]
                combination.append(j + 1)

        # Jika total bobot kombinasi ini valid dan nilainya lebih besar dari solusi sebelumnya
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combination = combination

    return max_value, best_combination

# Data input
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

# Panggil fungsi
max_value, best_combination = knapsack_bruteforce(values, weights, capacity)
print(f"Nilai maksimum: {max_value}")
print(f"Item yang dipilih: {best_combination}")

def knapsack_dp(values, weights, capacity):
    n = len(values)
    # Membuat tabel DP (n+1) x (capacity+1)
    DP = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    print(DP)
    '''
    [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 160, 160, 160, 160, 160, 160, 160, 160, 160, 160, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 220]
    ]

    '''

    # Mengisi tabel DP
    for i in range(1, n + 1): # perulangan baris matrik
        for w in range(1, capacity + 1): # perulangan kolom matrik
            if weights[i - 1] <= w:  # Jika bobot item ke-i bisa diambil
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]
    print(DP)
    # Nilai maksimum yang bisa diperoleh dengan kapasitas yang diberikan
    return DP[n][capacity]

# Data input
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

# Panggil fungsi DP
max_value = knapsack_dp(values, weights, capacity)
print(f"Nilai maksimum (DP): {max_value}")


# Dynamic Programming approach for 0/1 Knapsack Problem

def knapsack(n, weights, values, capacity):
    # Create a 2D array to store the maximum value at each n and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Populate the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # To find the items to include in the knapsack
    max_value = dp[n][capacity]
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if max_value <= 0:
            break
        if max_value == dp[i - 1][w]:
            continue
        else:
            selected_items.append(i - 1)  # Add item index
            max_value -= values[i - 1]
            w -= weights[i - 1]

    selected_items.reverse()
    total_weight = sum([weights[i] for i in selected_items])
    total_value = sum([values[i] for i in selected_items])

    return selected_items, total_weight, total_value

# Input example
n = int(input("Enter the number of items in the knapsack: "))
weights = list(map(int, input("Please enter the weight of each item: ").split()))
values = list(map(int, input("Please enter the value of each item: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

selected_items, total_weight, total_value = knapsack(n, weights, values, capacity)

print(f"Output: ({selected_items}, {total_weight}, {total_value})")
