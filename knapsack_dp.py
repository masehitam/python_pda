# basic
'''
1. 0/1 Knapsack Problem – Basic

Diberikan:

	•	Kapasitas: 10 kg
	•	Items: (Bobot, Nilai) = [(2, 3), (4, 5), (5, 8), (3, 4)]

Tentukan kombinasi item mana yang dapat dimasukkan ke dalam knapsack sehingga total nilainya maksimal tanpa melebihi kapasitas 10 kg.
'''
def knapsack_01(weights, values, capacity):
    n = len(values)
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]
    return DP[n][capacity]

weights = [2, 4, 5, 3]
values = [3, 5, 8, 4]
capacity = 10
print("Nilai maksimum:", knapsack_01(weights, values, capacity))

'''
2. Knapsack dengan Item Tidak Terbatas (Unbounded Knapsack)

Diberikan:

	•	Kapasitas: 50 kg
	•	Items: (Bobot, Nilai) = [(10, 60), (20, 100), (30, 120)]

Kamu dapat mengambil jumlah item yang sama lebih dari satu kali. Cari nilai maksimum yang bisa kamu capai dengan bobot maksimum 50 kg.
'''
def unbounded_knapsack(weights, values, capacity):
    n = len(values)
    DP = [0] * (capacity + 1)
    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                DP[w] = max(DP[w], DP[w - weights[i]] + values[i])
    return DP[capacity]

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Nilai maksimum:", unbounded_knapsack(weights, values, capacity))

def knapsack_unbounded(weights, values, capacity):
    n = len(values)
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]
    return DP[n][capacity]

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Nilai maksimum:", knapsack_unbounded(weights, values, capacity))

'''
3. 0/1 Knapsack dengan Item Terbatas (Bounded Knapsack)

Diberikan:

	•	Kapasitas: 50 kg
	•	Items: (Bobot, Nilai) = [(10, 60), (20, 100), (30, 120)]

Kamu dapat mengambil jumlah item yang sama lebih dari satu kali. Cari nilai maksimum yang bisa kamu capai dengan bobot maksimum 50 kg.
'''

def knapsack_bounded(weights, values, capacity):
    n = len(values)
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]
    return DP[n][capacity]

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Nilai maksimum:", knapsack_bounded(weights, values, capacity))

'''
4. 0/1 Knapsack dengan Item Terbatas (Bounded Knapsack) dengan DP

Diberikan:

	•	Kapasitas: 50 kg
	•	Items: (Bobot, Nilai) = [(10, 60), (20, 100), (30, 120)]

Kamu dapat mengambil jumlah item yang sama lebih dari satu kali. Cari nilai maksimum yang bisa kamu capai dengan bobot maksimum 50 kg.
'''
def knapsack_bounded_dp(weights, values, capacity):
    n = len(values)
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]
    return DP[n][capacity]

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Nilai maksimum:", knapsack_bounded_dp(weights, values, capacity))

'''
5. 0/1 Knapsack dengan Item Terbatas (Bounded Knapsack) dengan DP dan greedy

Diberikan:

	•	Kapasitas: 50 kg
	•	Items: (Bobot, Nilai) = [(10, 60), (20, 100), (30, 120)]

Kamu dapat mengambil jumlah item yang sama lebih dari satu kali. Cari nilai maksimum yang bisa kamu capai dengan bobot maksimum 50 kg.
'''
def knapsack_bounded_greedy(weights, values, capacity):
    n = len(values)
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]
    return DP[n][capacity]

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Nilai maksimum:", knapsack_bounded_greedy(weights, values, capacity))    # Output: 120

'''
3. Fractional Knapsack Problem

Diberikan:

	•	Kapasitas: 20 kg
	•	Items: (Bobot, Nilai) = [(5, 10), (10, 40), (15, 45), (5, 10)]

Kamu bisa memilih item secara parsial. Tentukan nilai maksimum yang bisa didapatkan.
'''
def fractional_knapsack(weights, values, capacity):
    items = sorted([(values[i] / weights[i], weights[i], values[i]) for i in range(len(values))], reverse=True)
    total_value = 0
    for ratio, weight, value in items:
        if capacity - weight >= 0:
            capacity -= weight
            total_value += value
        else:
            total_value += ratio * capacity
            break
    return total_value

weights = [5, 10, 15, 5]
values = [10, 40, 45, 10]
capacity = 20
print("Nilai maksimum:", fractional_knapsack(weights, values, capacity))

def fractional_knapsack(values, weights, capacity):
    n = len(values)
    items = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    for ratio, value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break

    return total_value

weights = [5, 10, 15]
values = [10, 40, 45]
capacity = 20
print("Nilai maksimum:", fractional_knapsack(values, weights, capacity))    # Output: 45

'''
4. Fractional Knapsack Problem dengan DP

Diberikan:

	•	Kapasitas: 20 kg
	•	Items: (Bobot, Nilai) = [(5, 10), (10, 40), (15, 45), (5, 10)]

Kamu bisa memilih item secara parsial. Tentukan nilai maksimum yang bisa didapatkan.
'''
def fractional_knapsack_dp(values, weights, capacity):
    n = len(values)
    items = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    for ratio, value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break

    return total_value

weights = [5, 10, 15]
values = [10, 40, 45]
capacity = 20
print("Nilai maksimum:", fractional_knapsack_dp(values, weights, capacity))    # Output: 45
'''
4. 0/1 Knapsack dengan Nilai Minimum

Diberikan:

	•	Kapasitas: 15 kg
	•	Items: (Bobot, Nilai) = [(3, 9), (5, 14), (4, 10), (6, 7)]

Pilih kombinasi item yang total bobotnya tidak melebihi 15 kg dan hasilkan total nilai minimum yang mungkin.
'''
def knapsack_min(weights, values, capacity):
    n = len(values)
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]
    return DP[n][capacity]

weights = [3, 4, 5, 6]
values = [9, 10, 14, 7]
capacity = 15
print("Nilai minimum:", knapsack_min(weights, values, capacity))    # Output: 7

def min_value_knapsack(weights, values, capacity):
    n = len(values)
    DP = [[float('inf')] * (capacity + 1) for _ in range(n + 1)]
    DP[0][0] = 0
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            DP[i][w] = DP[i - 1][w]
            if w >= weights[i - 1]:
                DP[i][w] = min(DP[i][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
    return min(DP[n][w] for w in range(capacity + 1) if DP[n][w] != float('inf'))

weights = [3, 5, 4, 6]
values = [9, 14, 10, 7]
capacity = 15
print("Nilai minimum:", min_value_knapsack(weights, values, capacity))
'''
5. Multiple Knapsack Problem

Diberikan:

	•	Kapasitas Knapsack 1: 10 kg
	•	Kapasitas Knapsack 2: 7 kg
	•	Items: (Bobot, Nilai) = [(5, 10), (4, 7), (6, 8), (3, 5), (2, 3)]

Temukan kombinasi item yang menghasilkan total nilai maksimum untuk dua knapsack tersebut.
'''
def multiple_knapsack(weights1, values1, weights2, values2, capacity1, capacity2):
    n1 = len(values1)
    n2 = len(values2)
    DP = [[0] * (capacity1 + 1) for _ in range(n1 + 1)]
    DP2 = [[0] * (capacity2 + 1) for _ in range(n2 + 1)]
    for i in range(1, n1 + 1):
        for w in range(1, capacity1 + 1):
            if weights1[i - 1] <= w:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights1[i - 1]] + values1[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]
    for i in range(1, n2 + 1):
        for w in range(1, capacity2 + 1):
            if weights2[i - 1] <= w:
                DP2[i][w] = max(DP2[i - 1][w], DP2[i - 1][w - weights2[i - 1]] + values2[i - 1])
            else:
                DP2[i][w] = DP2[i - 1][w]
    return DP[n1][capacity1] + DP2[n2][capacity2]

weights1 = [5, 4, 6, 3, 2]
values1 = [10, 7, 8, 5, 3]
weights2 = [2, 3, 4, 5, 6]
values2 = [3, 5, 8, 10, 7]
capacity1 = 10
capacity2 = 7
print("Nilai maksimum:", multiple_knapsack(weights1, values1, weights2, values2, capacity1, capacity2))

'''
Knapsack dengan Target Nilai

Diberikan:

	•	Kapasitas: 20 kg
	•	Items: (Bobot, Nilai) = [(6, 13), (4, 8), (7, 12), (3, 7)]
	•	Target Nilai: 20

Tentukan apakah mungkin mencapai target nilai 20 tanpa melebihi kapasitas, dan jika ya, sebutkan kombinasi itemnya.
'''
def knapsack_target(weights, values, capacity, target):
    n = len(values)
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]
    return DP[n][capacity]

weights = [6, 4, 7, 3]
values = [13, 8, 12, 7]
capacity = 20
target = 20
print("Target:", knapsack_target(weights, values, capacity, target))

def knapsack_with_target(weights, values, capacity, target_value):
    n = len(values)
    DP = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                DP[i][w] = DP[i - 1][w]
    # Check if target value can be achieved
    for w in range(capacity + 1):
        if DP[n][w] == target_value:
            return f"Target nilai {target_value} bisa dicapai dengan bobot total {w}."
    return "Target nilai tidak dapat dicapai."

weights = [6, 4, 7, 3]
values = [13, 8, 12, 7]
capacity = 20
target_value = 20
print(knapsack_with_target(weights, values, capacity, target_value))
