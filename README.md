# Cloud Proje - Multi-Container Docker Uygulaması

Bu proje, frontend ve backend olmak üzere iki ayrı Docker container'ında çalışan bir Flask uygulamasıdır. İçerisinde interaktif bir sayı tahmin oyunu bulunmaktadır.

## 🚀 Özellikler

- **Frontend Container**: Modern, responsive web arayüzü (Port 5000)
- **Backend Container**: RESTful API servisi (Port 5001)
- **Sayı Tahmin Oyunu**: 1-100 arası sayı tahmin etme oyunu
- **Docker Compose**: Kolay deployment ve container orchestration

## 📁 Proje Yapısı

```
cloudProje/
├── app.py                 # Frontend Flask uygulaması
├── Dockerfile             # Frontend container image
├── requirements.txt       # Frontend bağımlılıkları
├── docker-compose.yml     # Multi-container orchestration
├── templates/             # HTML template dosyaları
│   └── index.html
├── static/                # Statik dosyalar (CSS, JS)
└── backend/               # Backend API servisi
    ├── app.py            # Backend Flask API
    ├── Dockerfile        # Backend container image
    └── requirements.txt  # Backend bağımlılıkları
```

## 🛠️ Kurulum ve Çalıştırma

### Gereksinimler

- Docker
- Docker Compose

### Adımlar

1. **Projeyi klonlayın veya indirin**

2. **Docker Compose ile tüm servisleri başlatın:**

```bash
docker-compose up --build
```

Bu komut:
- Backend container'ını oluşturur ve 5001 portunda çalıştırır
- Frontend container'ını oluşturur ve 5000 portunda çalıştırır
- İki container'ı aynı network'te birleştirir

3. **Tarayıcınızda açın:**

- Frontend: http://localhost:5000
- Backend API: http://localhost:5001/api/health

### Diğer Komutlar

**Servisleri durdurmak:**
```bash
docker-compose down
```

**Servisleri arka planda çalıştırmak:**
```bash
docker-compose up -d
```

**Logları görüntülemek:**
```bash
docker-compose logs -f
```

**Belirli bir servisin loglarını görüntülemek:**
```bash
docker-compose logs -f frontend
docker-compose logs -f backend
```

## 🎮 Oyun Nasıl Oynanır?

1. Ana sayfada "Yeni Oyun" butonuna tıklayın
2. Backend 1 ile 100 arasında rastgele bir sayı seçer
3. Tahmininizi girin ve "Tahmin Et" butonuna tıklayın
4. Backend size ipucu verir:
   - ⬆️ Daha yüksek bir sayı deneyin
   - ⬇️ Daha düşük bir sayı deneyin
   - 🎉 Doğru tahmin! (Oyun biter)

## 🔧 API Endpoints

### Backend API Endpoints

- `GET /api/health` - Backend sağlık kontrolü
- `POST /api/game/start` - Yeni oyun başlat
- `POST /api/game/guess` - Tahmin yap
- `GET /api/game/status/<game_id>` - Oyun durumunu kontrol et
- `POST /api/game/end/<game_id>` - Oyunu bitir

## 🐳 Container Detayları

### Frontend Container
- **Port**: 5000
- **Framework**: Flask
- **Template Engine**: Jinja2
- **Frontend**: Tailwind CSS, JavaScript

### Backend Container
- **Port**: 5001
- **Framework**: Flask
- **CORS**: flask-cors ile aktif
- **Oyun Mantığı**: In-memory oyun durumu yönetimi

## 📝 Notlar

- Backend ve frontend ayrı container'larda çalışır
- Container'lar Docker Compose network'ü üzerinden iletişim kurar
- Frontend, backend'e `backend:5001` adresi üzerinden bağlanır
- Local development için frontend `localhost:5001` kullanır

## 🔍 Sorun Giderme

**Backend'e bağlanamıyorum:**
- `docker-compose ps` ile container'ların çalıştığından emin olun
- `docker-compose logs backend` ile backend loglarını kontrol edin

**Frontend açılmıyor:**
- Port 5000'in kullanımda olmadığından emin olun
- `docker-compose logs frontend` ile frontend loglarını kontrol edin

## 📄 Lisans

Bu proje eğitim amaçlıdır.


Mehmet Efe Ergin 220201024
Yusuf Berk Baytok 220201023
Anıl Akpınar 220201013
