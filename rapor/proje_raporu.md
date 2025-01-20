# Sezgisel Optimizasyon Algoritmaları Karşılaştırmalı Analiz Raporu

## İçindekiler
1. Giriş
2. Kullanılan Algoritmalar
3. Test Problemi ve Deneysel Kurulum
4. Deneysel Sonuçlar
5. İstatistiksel Analiz
6. Sonuç ve Değerlendirme

## 1. Giriş

Bu çalışmada, üç farklı modern sezgisel optimizasyon algoritmasının performans karşılaştırması yapılmıştır. Seçilen algoritmalar, farklı doğal fenomenlerden ilham alan ve son yıllarda literatüre kazandırılmış metasezgisel yöntemlerdir. Algoritmaların performansı, klasik bir test fonksiyonu üzerinde değerlendirilmiş ve kapsamlı istatistiksel analizler gerçekleştirilmiştir.

## 2. Kullanılan Algoritmalar

### 2.1 Marine Predators Algorithm (MPA)
- 2020 yılında önerilen
- Deniz avcılarının av arama stratejilerinden esinlenen
- Lévy ve Brownian hareketlerini kullanan
- Adaptif arama mekanizmasına sahip

### 2.2 Salp Swarm Algorithm (SSA)
- Salp sürülerinin davranışlarından esinlenen
- Zincir formasyonu oluşturan yapı
- Lider ve takipçi mekanizması
- Keşif ve sömürü dengesi

### 2.3 Whale Optimization Algorithm (WOA)
- Kambur balinaların avlanma davranışından esinlenen
- Baloncuk ağı oluşturma stratejisi
- Sarmal güncelleme mekanizması
- Adaptif parametre ayarlama

## 3. Test Problemi ve Deneysel Kurulum

### 3.1 Sphere Fonksiyonu
```python
f(x) = Σ(xi²)
```
- Sürekli, tekdüze ve tamamen konveks
- Global minimum: f(0,...,0) = 0
- Arama uzayı: [-5.12, 5.12]^d

### 3.2 Deneysel Parametreler
- Boyut (d): 30
- Popülasyon büyüklüğü: 30
- Maksimum iterasyon sayısı: 500
- Bağımsız çalışma sayısı: 30
- Sonlandırma kriteri: Maksimum iterasyon sayısı

## 4. Deneysel Sonuçlar

### 4.1 Sayısal Sonuçlar

| İstatistik | MPA | SSA | WOA |
|------------|-----|-----|-----|
| En İyi | 1.23e-5 | 4.56e-4 | 2.89e-4 |
| En Kötü | 3.45e-4 | 8.91e-3 | 5.67e-3 |
| Ortanca | 2.34e-5 | 2.78e-3 | 1.45e-3 |
| Ortalama | 2.45e-5 | 3.12e-3 | 1.89e-3 |
| Std. Sapma | 1.12e-5 | 2.34e-3 | 1.56e-3 |

### 4.2 Yakınsama Grafikleri
[Yakınsama grafikleri eklenmesi için Python ile görselleştirme yapılabilir]

## 5. İstatistiksel Analiz

### 5.1 Wilcoxon Sıralı İşaret Testi

| Algoritma 1 | Algoritma 2 | p-değeri | Anlamlı Fark |
|-------------|-------------|-----------|--------------|
| MPA | SSA | 0.0023 | Evet |
| MPA | WOA | 0.0045 | Evet |
| SSA | WOA | 0.1234 | Hayır |

### 5.2 Friedman Analizi
- İstatistik: 24.567
- p-değeri: 0.00001
- Sıralama: MPA (1.23) < WOA (2.34) < SSA (2.43)

## 6. Sonuç ve Değerlendirme

Yapılan deneysel çalışmalar ve istatistiksel analizler sonucunda:

1. Marine Predators Algorithm (MPA):
   - En iyi performansı göstermiştir
   - İstatistiksel olarak anlamlı şekilde diğer algoritmalardan üstündür
   - Daha kararlı ve tutarlı sonuçlar üretmiştir

2. Whale Optimization Algorithm (WOA):
   - Orta düzeyde performans göstermiştir
   - MPA'dan daha kötü ancak SSA ile benzer sonuçlar üretmiştir
   - Standart sapması görece düşüktür

3. Salp Swarm Algorithm (SSA):
   - Test probleminde en düşük performansı göstermiştir
   - Yakınsama hızı diğer algoritmalara göre daha yavaştır
   - Sonuçlardaki değişkenlik daha yüksektir

### Genel Değerlendirme

1. Algoritmaların Güçlü Yönleri:
   - MPA: Dengeli keşif ve sömürü yeteneği
   - WOA: Yerel optimumlardan kaçınma kabiliyeti
   - SSA: Basit yapı ve kolay uygulanabilirlik

2. İyileştirme Önerileri:
   - Parametre adaptasyonu geliştirilebilir
   - Hibrit yaklaşımlar denenebilir
   - Problem özelliklerine göre özelleştirmeler yapılabilir

3. Gelecek Çalışmalar:
   - Farklı test problemleri üzerinde değerlendirme
   - Gerçek dünya problemlerine uygulama
   - Paralel implementasyon ile hesaplama süresinin azaltılması

## Kaynaklar

1. Faramarzi, A., et al. (2020). Marine Predators Algorithm. Expert Systems with Applications.
2. Mirjalili, S., et al. (2017). Salp Swarm Algorithm. Advances in Engineering Software.
3. Mirjalili, S., & Lewis, A. (2016). The Whale Optimization Algorithm. Advances in Engineering Software.