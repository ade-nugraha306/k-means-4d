import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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


file_txt = "./dataset.txt"
hasil = baca_tabel_per_kolom(file_txt)

# Akses Setiap Kolom
print("No: ", hasil["No"])
print("Nama: ", hasil["Nama"])
print("Berat Badan: ", hasil["BeratBadan"])
print("Tinggi Badan: ", hasil["TinggiBadan"])
print("Lingkar Pinggang: ", hasil["LingkarPinggang"])
print("Tekanan Darah: ", hasil["TekananDarah"])

x = hasil["BeratBadan"]
y = hasil["LingkarPinggang"]

plt.scatter(x, y)
plt.xlabel("Berat Badan (kg)")
plt.ylabel("Lingkar Pinggang (cm)")
plt.title("Scatter Plot Berat Badan vs Lingkar Pinggang")
plt.show()

data = list(zip(x, y))
inertias = []

for i in range(1,10):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,10), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=4)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()