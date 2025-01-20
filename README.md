# Sezgisel Optimizasyon Algoritmaları Karşılaştırma Projesi

Bu proje, üç farklı sezgisel optimizasyon algoritmasının performansını karşılaştırmaktadır:
1. Marine Predators Algorithm (MPA)
2. Salp Swarm Algorithm (SSA)
3. Whale Optimization Algorithm (WOA)

## Proje Yapısı

```
sezgisel/
│
├── algoritmalar/
│   ├── mpa.py
│   ├── ssa.py
│   └── woa.py
│
├── problem/
│   └── benchmark.py
│
├── sonuclar/
│
├── rapor/
│
└── main.py
```

## Gereksinimler

- Python 3.7+
- NumPy
- SciPy
- Pandas

## Kurulum

Gerekli Python paketlerini yüklemek için:

```bash
pip install numpy scipy pandas
```

## Kullanım

1. `main.py` dosyasında test parametrelerini ayarlayın:
   - `selected_function`: 'sphere', 'rosenbrock', veya 'rastrigin'
   - `dimension`: problem boyutu
   - `population_size`: popülasyon büyüklüğü
   - `max_iterations`: maksimum iterasyon sayısı

2. Programı çalıştırın:
```bash
python main.py
```

3. Sonuçlar `sonuclar/` klasöründe kaydedilecektir.

## Sonuçlar

Program çalıştırıldığında aşağıdaki sonuçlar elde edilir:
- Her algoritma için en iyi, en kötü, ortanca, ortalama ve standart sapma değerleri
- Wilcoxon sıralı işaret testi sonuçları
- Friedman analizi sonuçları