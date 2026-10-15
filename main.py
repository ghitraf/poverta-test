from fastapi import FastAPI
import logging
import sys

# Setup Logging agar terbaca oleh Promtail/Loki
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="Poverta App", version="1.0.0")

@app.get("/")
def read_root():
    logger.info("User mengakses halaman utama")
    return {"message": "Halo! Ini adalah Poverta App V2 - CI/CD BERHASIL."}

@app.get("/health")
def health_check():
    # Endpoint ini penting untuk Uptime Kuma & CI/CD
    return {"status": "healthy"}

@app.get("/login/{username}")
def login_user(username: str):
    logger.info(f"User {username} berhasil login")
    return {"message": f"Selamat datang, {username}!"}
