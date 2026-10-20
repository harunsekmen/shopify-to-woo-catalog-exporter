# 🚀 Shopify'dan WooCommerce'e Yüksek Sadakatli Katalog Taşıyıcı

[🇬🇧 English](README.md) · [🇹🇷 Türkçe](README.tr.md)

> Shopify ürünlerini, varyantlarını, görsellerini, meta alanlarını ve SEO URL yapılarını WooCommerce'e veri kaybı olmadan aktaran yüksek performanslı göç aracı.

Geliştirici ve Bakım Sorumlusu: **[Harun Sekmen](https://github.com/harunsekmen)** — E-Ticaret Sistem Mühendisi & WooCommerce Uzmanı.

[✉️ İletişime Geç](mailto:sekmenwp@gmail.com) · [💼 Upwork Profili](https://www.upwork.com/freelancers/~01a7a8b58043e6e6d9) · [🔗 GitHub Ana Profil](https://github.com/harunsekmen)

---

## ⚡ Çözdüğü Kritik Sorun

Shopify'dan WooCommerce'e geçiş yapan işletmelerin yaşadığı en büyük sancı veri aktarımıdır:
- Standart CSV içe aktarıcılar çoklu varyantları ve özel meta alanları kırar.
- Görsel bağlantıları ve galeri sıralamaları kaybolur.
- Değişen URL yapıları nedeniyle mevcut Google sıralamaları ve organik trafik sıfırlanır.

Bu araç, Shopify GraphQL/REST API'si ile WooCommerce REST API'si arasında doğrudan köprü kurarak eksiksiz taşıma sağlar.

---

## 🛠️ Öne Çıkan Özellikler

- **Varyant ve Seçenek Koruması:** Renk, beden ve özel seçenekleri WooCommerce ürün niteliklerine kayıpsız dönüştürür.
- **Görsel ve Medya İndirme:** Ürün görsellerini doğrudan WordPress ortam kütüphanesine aktarır ve öne çıkan görseli ayarlar.
- **SEO Yönlendirme Haritası:** Eski Shopify URL'lerini yeni WooCommerce bağlantılarına 301 yönlendirmesiyle bağlar.
- **Toplu İşlem & Hata Yakalama:** Yarıda kalan aktarımları kaldığı yerden devam ettiren güvenli kuyruk mekanizması.

---

## 🏗️ Teknik Mimari ve Standartlar

`Python 3.10+` • `Shopify Admin API` • `WooCommerce REST API` • `Pydantic`

---

## 🚀 Kurulum ve Test

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/harunsekmen/shopify-to-woo-catalog-exporter.git
   cd shopify-to-woo-catalog-exporter && python3 tests/test_migrator.py
   ```

---

## 📄 Lisans

Bu proje **GPL-3.0 Lisansı** ile açık kaynak olarak sunulmaktadır.
