import csv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def baca_tabel_per_kolom(file_path):
    kolom = {}
    with open(file_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for h in reader.fieldnames:
            kolom [h] = []
        
        for row in reader:
            for h in reader.fieldnames:
                value = row[h]
                if value.isdigit():
                    kolom[h].append(int(value))
                else:
                    kolom[h].append(value)
                
    return kolom

# Main 
file_txt = "./dataset.csv"
hasil = baca_tabel_per_kolom(file_txt)

# Akses Setiap Kolom
print("No: ", hasil["No"])
print("Nama: ", hasil["Nama"])
print("Berat Badan: ", hasil["BeratBadan"])
print("Tinggi Badan: ", hasil["TinggiBadan"])
print("Lingkar Pinggang: ", hasil["LingkarPinggang"])
print("Tekanan: ", hasil["TekananDarah"])

x = hasil["BeratBadan"]
y = hasil["LingkarPinggang"]

plt.scatter(x, y)
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