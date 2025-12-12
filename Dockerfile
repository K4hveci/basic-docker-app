# Frontend Container
FROM python:3.9-slim

WORKDIR /app

# Gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kodunu ve template dosyalarını içeri kopyala
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/

# Port'u expose et (Frontend 5000 portunda çalışıyor)
EXPOSE 5000

# Uygulamayı başlat
CMD ["python", "app.py"]