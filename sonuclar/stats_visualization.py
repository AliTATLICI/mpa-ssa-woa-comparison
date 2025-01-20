import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# .npy dosyasını yükle
data = np.load("sphere_20250120_224259_raw.npy", allow_pickle=True)
data_dict = data.item()

# Figürleri oluştur (2x2 layout)
fig = plt.figure(figsize=(15, 12))

# 1. Alt grafik: Algoritmaların performans karşılalaştırması (Box plot)
plt.subplot(2, 2, 1)
algorithms = ['MPA', 'SSA', 'WOA']
values = [data_dict[alg] for alg in algorithms]
plt.boxplot(values, labels=algorithms)
plt.title('Algoritma Performans Karşılaştırmaları')
plt.ylabel('Fitness Değeri')
plt.yscale('log')  # Logaritmik ölçek kullan

# 2. Alt grafik: Ortalama performans karşılaştırmaları (Bar plot)
plt.subplot(2, 2, 2)
averages = [np.mean(data_dict[alg]) for alg in algorithms]
plt.bar(algorithms, averages)
plt.title('Ortalama Performans')
plt.ylabel('Ortalama Fitness Değeri')
plt.yscale('log')

# 3. Alt grafik: En iyi değerler (Bar plot)
plt.subplot(2, 2, 3)
best_values = [np.min(data_dict[alg]) for alg in algorithms]
plt.bar(algorithms, best_values)
plt.title('En İyi Değerler')
plt.ylabel('En İyi Fitness Değeri')
plt.yscale('log')

# 4. Alt grafik: Standart sapma (Bar plot)
plt.subplot(2, 2, 4)
std_values = [np.std(data_dict[alg]) for alg in algorithms]
plt.bar(algorithms, std_values)
plt.title('Standart Sapma')
plt.ylabel('Standart Sapma Değeri')
plt.yscale('log')

# Genel başlık ekle
plt.suptitle('Sphere Fonksiyonu Optimizasyon Sonuçları', fontsize=16)

# Grafiklerin düzenini ayarla
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Dosyayı kaydet
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"stats_visualization_{timestamp}.png"
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.show()

print(f"İstatistik görseli '{filename}' olarak kaydedildi.")