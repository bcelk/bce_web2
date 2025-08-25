from flask import Flask

# Flask uygulaması oluştur
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ BCE analiz sistemi Render üzerinde çalışıyor!"

# Render otomatik gunicorn ile başlatıyor, ama local test için:
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
