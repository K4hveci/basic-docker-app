# Backend Container
FROM python:3.9-slim

WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY app.py .

# Port'u expose et (Backend 5001 portunda çalışıyor)
EXPOSE 5001

# Uygulamayı başlat
CMD ["python", "app.py"]

