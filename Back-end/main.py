import http.server
import ssl
import os

# --- Configuration ---
PORT = 4443
BASE_DIR = os.path.dirname(__file__)
FRONT_DIR = os.path.join(BASE_DIR, "../Front-end")
CERT_PATH = os.path.join(BASE_DIR, "../certs-cryptography/certs/certificate.pem")
KEY_PATH = os.path.join(BASE_DIR, "../certs-cryptography/certs/private_key.pem")

# --- Vérification des certificats ---
if not (os.path.exists(CERT_PATH) and os.path.exists(KEY_PATH)):
    raise FileNotFoundError("Certificat ou clé privée manquante dans 'certs-cryptography/certs/'")

# --- Vérifie que le dossier Front-end contient index.html ---
if not os.path.exists(os.path.join(FRONT_DIR, "index.html")):
    raise FileNotFoundError("Fichier index.html introuvable dans le dossier 'Front-end/'")

# --- Changer le répertoire courant ---
os.chdir(FRONT_DIR)

# --- Serveur HTTPS moderne ---
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('localhost', PORT), handler)

# 🔒 Créer un contexte SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_PATH, keyfile=KEY_PATH)

# 🧠 Remplace l’ancien wrap_socket
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"✅ Serveur HTTPS démarré sur https://localhost:{PORT}")
print(f"📂 Fichiers servis depuis : {FRONT_DIR}")

httpd.serve_forever()
