# ⚡ STerm - Terminal Ecosystem

![Serix OS Badge](https://img.shields.io/badge/Serix_OS-Amber-orange?style=for-the-badge)
![Development](https://img.shields.io/badge/Developed_by-Kapsül_Serix_Takımı-00ccff?style=for-the-badge)

**STerm**, Serix OS Amber ekosistemi için **Kapsül Serix Takımı** tarafından sıfırdan tasarlanmış gelişmiş bir terminal katmanıdır. Sistem yönetimi, paket kontrolü ve grafik arayüz geçişlerini tek bir merkezden yöneterek kullanıcıya kusursuz bir hibrit deneyim sunar.

## 🛠️ Teknik Özellikler

* **Hybrid Core:** Debian (Ubuntu) ve Arch tabanlı sistemlerde otomatik uyumluluk ve paket yöneticisi tespiti.
* **Serix-Get:** Paket yönetim süreçlerini optimize eden, hata payını minimize eden özel komut seti.
* **Amber GUI Dashboard:** Terminal üzerinden `gui` komutuyla tetiklenebilen, grafiksel kontrol paneli desteği.
* **System Metrics:** Donanım (RAM/Disk) ve ağ durumunu izleyen entegre `system-check` ve `speed-test` araçları.

## 🚀 Kurulum ve Kullanım

Sistemi klonlamak ve çalıştırmak için terminalinize aşağıdaki komutları girin:

```bash
# Depoyu klonlayın
git clone https://github.com/kefe3/sterm.git

# Klasöre giriş yapın
cd sterm

# Çalıştırma izni verin
chmod +x sterm.py

# Terminali başlatın
./sterm.py
⌨️ Özel KomutlarKomutİşlevserix-get [paket]Sisteminize uygun paket yükleyiciyi çalıştırır.guiKapsül Serix grafiksel yönetim panelini açar.system-checkKaynak kullanımını (CPU/RAM/Disk) analiz eder.speed-testİnternet bağlantı hızınızı ölçer.helpTüm özel komutların listesini görüntüler.🛡️ Geliştirici EkipBu yazılımın tüm hakları ve geliştirme süreçleri Kapsül Serix Takımı'na aittir. Serix OS Amber'ın çekirdek bileşenlerini geliştirmek ve kullanıcı deneyimini en üst seviyeye çıkarmak için çalışıyoruz.Maintained by: kefe3
