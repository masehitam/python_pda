'''
1. Linear Programming Problem – Factory Production

Sebuah pabrik memproduksi dua jenis produk: A dan B. Produk tersebut dijual dengan keuntungan Rp 30 untuk produk A dan Rp 20 untuk produk B. Untuk memproduksi produk A, dibutuhkan 2 jam pada mesin 1 dan 3 jam pada mesin 2. Untuk memproduksi produk B, dibutuhkan 4 jam pada mesin 1 dan 2 jam pada mesin 2. Setiap hari, mesin 1 hanya dapat digunakan selama 100 jam, dan mesin 2 hanya selama 80 jam.

	•	Berapa banyak produk A dan B yang harus diproduksi untuk memaksimalkan keuntungan?
	•	Apa keuntungan maksimum yang dapat diperoleh?
'''
from scipy.optimize import linprog

# Koefisien fungsi objektif (negatif karena kita memaksimalkan keuntungan)
c = [-30, -20]

# Koefisien kendala (waktu penggunaan mesin 1 dan 2)
A = [[2, 4], [3, 2]]

# Kapasitas mesin (jam)
b = [100, 80]

# Membatasi produksi tidak boleh negatif
x_bounds = (0, None)

# Menyelesaikan masalah linear programming
res = linprog(c, A_ub=A, b_ub=b, bounds=(x_bounds, x_bounds), method='highs')

print("Jumlah produk A:", res.x[0])
print("Jumlah produk B:", res.x[1])
print("Keuntungan maksimum:", -res.fun)
'''
2. Job Scheduling Problem

Ada lima pekerjaan yang harus diselesaikan dengan masing-masing tenggat waktu dan keuntungan terkait yang akan diperoleh jika pekerjaan selesai tepat waktu:

Pekerjaan	Tenggat Waktu (hari)	Keuntungan (Rp)
A	2	1000
B	1	500
C	2	800
D	1	600
E	3	1200

	•	Tentukan pekerjaan mana yang harus dilakukan untuk memaksimalkan keuntungan, dengan asumsi bahwa hanya satu pekerjaan dapat dilakukan pada satu waktu.
'''
def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    schedule = [None] * max_deadline
    total_profit = 0

    for job in jobs:
        for t in range(job[1] - 1, -1, -1):
            if schedule[t] is None:
                schedule[t] = job[0]
                total_profit += job[2]
                break

    return schedule, total_profit

jobs = [('A', 2, 1000), ('B', 1, 500), ('C', 2, 800), ('D', 1, 600), ('E', 3, 1200)]
schedule, total_profit = job_scheduling(jobs)
print("Jadwal pekerjaan:", schedule)
print("Keuntungan maksimum:", total_profit)
'''
3. Transportation Problem

Sebuah perusahaan logistik ingin mengirim barang dari tiga gudang ke empat pusat distribusi. Kapasitas pengiriman dari masing-masing gudang dan permintaan masing-masing pusat distribusi adalah sebagai berikut:

Gudang	Kapasitas (unit)
W1	20
W2	30
W3	25

Pusat Distribusi	Permintaan (unit)
D1	10
D2	25
D3	15
D4	25

Biaya pengiriman (dalam ribu Rupiah) dari setiap gudang ke setiap pusat distribusi adalah:

	D1	D2	D3	D4
W1	8	6	10	9
W2	9	12	13	7
W3	14	9	16	5

	•	Tentukan skema pengiriman yang meminimalkan biaya total.
'''
from scipy.optimize import linprog

# Koefisien biaya pengiriman
cost = [8, 6, 10, 9, 9, 12, 13, 7, 14, 9, 16, 5]

# Kapasitas gudang (sisi supply)
supply = [20, 30, 25]

# Permintaan pusat distribusi (sisi demand)
demand = [10, 25, 15, 25]

# Membuat kendala untuk supply (<= kapasitas gudang)
A_eq = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

# Membuat kendala untuk demand (>= permintaan)
b_eq = supply

# Permintaan harus terpenuhi (>= demand)
A_ub = [[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]]

b_ub = demand

res = linprog(cost, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, method='highs')

print("Skema pengiriman:", res.x.reshape((3, 4)))
print("Biaya total:", res.fun)
'''
4. Network Flow Optimization Problem

Sebuah perusahaan memiliki lima pusat distribusi yang terhubung oleh jalan-jalan. Kapasitas maksimum pengiriman barang di sepanjang jalan-jalan ini (dalam unit per hari) digambarkan sebagai berikut:

	•	Dari A ke B: 20 unit
	•	Dari A ke C: 15 unit
	•	Dari B ke D: 10 unit
	•	Dari C ke D: 25 unit
	•	Dari C ke E: 10 unit
	•	Dari D ke E: 15 unit
	•	Tentukan jumlah maksimum barang yang dapat dikirim dari pusat distribusi A ke E setiap harinya.
'''
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.capacity = {}

    def add_edge(self, u, v, cap):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = cap
        self.capacity[(v, u)] = 0

    def bfs(self, s, t, parent):
        visited = [False] * (self.V)
        queue = [s]
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if visited[v] == False and self.capacity[(u, v)] > 0:
                    parent[v] = u
                    if v == t:
                        return True
                    queue.append(v)
                    visited[v] = True
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.V)
        max_flow = 0
        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.capacity[(parent[s], s)])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.capacity[(u, v)] -= path_flow
                self.capacity[(v, u)] += path_flow
                v = parent[v]
        return max_flow

g = Graph(5)
g.add_edge(0, 1, 20)
g.add_edge(0, 2, 15)
g.add_edge(1, 3, 10)
g.add_edge(2, 3, 25)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 15)

source = 0
sink = 4

print("Aliran maksimum:", g.ford_fulkerson(source, sink))
'''
5. Investment Portfolio Optimization

Anda memiliki anggaran Rp 1.000.000 untuk diinvestasikan di tiga jenis saham yang memiliki return dan risiko yang berbeda:

	•	Saham A: Return harian 2%, Risiko 1%
	•	Saham B: Return harian 3%, Risiko 1.5%
	•	Saham C: Return harian 5%, Risiko 3%

Anda ingin memaksimalkan return harian, tetapi dengan syarat total risiko dari investasi tidak lebih dari 2.5%. Berapa banyak uang yang harus diinvestasikan di masing-masing saham untuk mencapai tujuan tersebut?
'''
from scipy.optimize import minimize

# Data return dan risiko
returns = [0.02, 0.03, 0.05]
risks = [0.01, 0.015, 0.03]

# Fungsi objektif untuk memaksimalkan return
def objective(x):
    return -(x[0]*returns[0] + x[1]*returns[1] + x[2]*returns[2])

# Kendala risiko tidak boleh melebihi 2.5%
def constraint(x):
    return 2.5 - (x[0]*risks[0] + x[1]*risks[1] + x[2]*risks[2])

# Total investasi tidak boleh melebihi Rp 1.000.000
def budget_constraint(x):
    return 1_000_000 - sum(x)

x0 = [0, 0, 0]
bounds = [(0, 1_000_000), (0, 1_000_000), (0, 1_000_000)]
cons = [{'type': 'ineq', 'fun': constraint}, {'type': 'eq', 'fun': budget_constraint}]

sol = minimize(objective, x0, bounds=bounds, constraints=cons)
print("Investasi di saham A:", sol.x[0])
print("Investasi di saham B:", sol.x[1])
print("Investasi di saham C:", sol.x[2])
print("Total return harian:", -sol.fun)
'''
6. Knapsack Problem – Extended

Anda memiliki kapasitas anggaran sebesar Rp 50.000 dan ada beberapa barang yang dapat dibeli di toko dengan harga dan nilai berikut:

Barang	Harga (Rp)	Nilai (unit)
A	15.000	10
B	20.000	15
C	10.000	8
D	25.000	20
E	30.000	25

	•	Tentukan barang-barang mana yang harus dibeli untuk memaksimalkan nilai yang didapatkan, dengan tetap berada di dalam anggaran.
'''
def knapsack_01(weights, values, capacity):
    n = len(values)
    DP = [0] * (capacity + 1)
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            DP[w] = max(DP[w], DP[w - weights[i]] + values[i])
    return DP[capacity]

weights = [15000, 20000, 10000, 25000, 30000]
values = [10, 15, 8, 20, 25]
capacity = 50000
print("Nilai maksimum:", knapsack_01(weights, values, capacity))
'''
7. Graph Optimization – Shortest Path

Sebuah kota memiliki lima lokasi penting yang terhubung dengan jalan sebagai berikut:

	•	Dari A ke B: 7 km
	•	Dari A ke C: 9 km
	•	Dari B ke D: 3 km
	•	Dari C ke D: 2 km
	•	Dari D ke E: 4 km
	•	Temukan rute terpendek dari A ke E.

Soal-soal ini mencakup berbagai aspek dari optimization problems, seperti linear programming, knapsack, job scheduling, dan transportation problems. Kamu bisa menggunakan berbagai teknik seperti dynamic programming, greedy algorithm, atau algoritma graf seperti Dijkstra’s untuk menyelesaikan soal-soal ini. Jika kamu butuh solusi untuk soal tertentu, beri tahu saya!
'''
import heapq

def dijkstra(graph, start, end):
    heap = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances[end]

graph = {

    'A': {'B': 10, 'C': 3},
    'B': {'D': 5},
    'C': {'B': 2, 'D': 8},
    'D': {}
}

print("Jarak terpendek dari A ke D:", dijkstra(graph, 'A', 'D'))