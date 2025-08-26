import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

def baca_tabel_per_kolom(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip().split("\t") for line in f if line.strip()]

    # Ambil header
    header = lines[0]

    # Ambil data isi table
    data = lines[1:]

    # Buat dictionary untuk menampung list per kolom
    kolom = {h: [] for h in header}

    # Isi dictionary dengan data sesuai kolom
    for row in data:
        for i, h in enumerate(header):
            value = row[i]
            # kalau bisa di-cast ke int, jadikan int
            if value.isdigit():
                kolom[h].append(int(value))
            else:
                kolom[h].append(value)

    return kolom


# Main 
file_txt = "./dataset.txt"
hasil = baca_tabel_per_kolom(file_txt)

# Akses Setiap Kolom
print("No: ", hasil["No"])
print("Nama: ", hasil["Nama"])
print("Berat Badan: ", hasil["BeratBadan"])
print("Tinggi Badan: ", hasil["TinggiBadan"])
print("Lingkar Pinggang: ", hasil["LingkarPinggang"])
print("Tekanan Darah: ", hasil["TekananDarah"])

# Scatter Plot: Berat Badan vs Lingkar Pinggang
x = hasil["BeratBadan"]
y = hasil["TinggiBadan"]
z = hasil["LingkarPinggang"]

# Buat figure dan axis 3D
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Scatter 3D
ax.scatter(x, y, z)

# Label axis
ax.set_xlabel("Berat Badan (kg)")
ax.set_ylabel("Tinggi Badan (cm)")
ax.set_zlabel("Lingkar Pinggang (cm)")

plt.title("Scatter Plot Berat Badan vs Tinggi Badan vs Lingkar Pinggang")
plt.show()

data = np.array(list(zip(x, y, z)))  # pastikan data array

silhouette_scores = []
inertias = []

# Silhouette (minimal cluster = 2)
for i in range(2, 10):
    kmeans = KMeans(n_clusters=i, n_init=10, random_state=42)
    kmeans.fit(data)
    labels = kmeans.labels_
    score = silhouette_score(data, labels)
    silhouette_scores.append(score)

# Elbow (mulai dari 1)
for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, n_init=10, random_state=42)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

# --- Plot ---
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Silhouette
axs[0].plot(range(2, 10), silhouette_scores, marker='o')
axs[0].set_title('Silhouette Score Method')
axs[0].set_xlabel('Number of clusters')
axs[0].set_ylabel('Silhouette Score')

# Elbow
axs[1].plot(range(1, 10), inertias, marker='o')
axs[1].set_title('Elbow Method')
axs[1].set_xlabel('Number of clusters')
axs[1].set_ylabel('Inertia')

plt.tight_layout()
plt.show()

# Ambil 3 kolom
x = hasil["BeratBadan"]
y = hasil["TinggiBadan"]
z = hasil["LingkarPinggang"]

# Bikin array 3D
data = np.array(list(zip(x, y, z)))

kmeans = KMeans(n_clusters=4)
kmeans.fit(data)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=labels, cmap='viridis', s=50)
ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], c='red', s=200, marker='X')

ax.set_xlabel('Berat Badan')
ax.set_ylabel('Tinggi Badan')
ax.set_zlabel('Lingkar Pinggang')
plt.show()