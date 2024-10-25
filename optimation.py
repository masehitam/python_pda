def activity_selection(start_times, end_times):
    n = len(start_times)
    selected_activities = []

    # Urutkan aktivitas berdasarkan waktu selesai
    activities = sorted(range(n), key=lambda i: end_times[i])

    # Aktivitas pertama selalu dipilih
    selected_activities.append(activities[0])
    last_finish_time = end_times[activities[0]]

    # Pilih aktivitas berikutnya yang tidak bentrok
    for i in range(1, n):
        if start_times[activities[i]] >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = end_times[activities[i]]

    return selected_activities

# Contoh penggunaan:
start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]

selected_activities = activity_selection(start_times, end_times)
print(f"Aktivitas yang dipilih: {selected_activities}")

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    mst = []
    uf = UnionFind(n)

    # Urutkan sisi berdasarkan bobot
    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))

    return mst

# Contoh penggunaan:
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
n = 4  # Jumlah simpul
mst = kruskal(n, edges)
print(f"Minimum Spanning Tree: {mst}")