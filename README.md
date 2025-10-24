# 🔐 Python Local HTTPS Server

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![HTTPS](https://img.shields.io/badge/HTTPS-SSL%2FTLS-green.svg)](https://tools.ietf.org/html/rfc2818)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Un serveur HTTPS local complet en Python avec certificats auto-signés, interface web moderne et architecture sécurisée. Parfait pour le développement local, les tests SSL/TLS et l'apprentissage de la cryptographie.

## 🎯 Fonctionnalités

- ✅ **Serveur HTTPS natif** avec `http.server` et SSL/TLS moderne
- 🔑 **Génération automatique de certificats** X.509 auto-signés
- 🌐 **Interface web responsive** avec design moderne
- 🔒 **Implémentation SSL sécurisée** avec `ssl.SSLContext`
- 📱 **Compatible mobile** avec design adaptatif
- 🛠️ **Notebooks Jupyter** pour tests interactifs

## 🏗️ Architecture du Système

```mermaid
graph TB
    subgraph "Client Browser"
        A[🌐 Web Browser] --> B[HTTPS Request]
    end
    
    subgraph "HTTPS Server"
        B --> C[🔒 SSL/TLS Layer]
        C --> D[📡 HTTP Server]
        D --> E[📁 Static File Handler]
    end
    
    subgraph "Frontend Files"
        E --> F[📄 index.html]
        E --> G[🎨 style.css]
        E --> H[⚡ script.js]
    end
    
    subgraph "Certificate Management"
        I[🔑 Certificate Generator] --> J[📜 certificate.pem]
        I --> K[🗝️ private_key.pem]
        J --> C
        K --> C
    end
    
    subgraph "Backend Logic"
        L[📓 main.ipynb] --> D
        M[🛠️ cert_generator.ipynb] --> I
    end
    
    style A fill:#e1f5fe
    style C fill:#f3e5f5
    style D fill:#e8f5e8
    style I fill:#fff3e0
```

## 🔧 Diagramme de Classes UML

```mermaid
classDiagram
    class HTTPSServer {
        +ssl_context: SSLContext
        +server_address: tuple
        +handler_class: SimpleHTTPRequestHandler
        +socket: socket
        +start_server()
        +stop_server()
        +load_certificates()
    }
    
    class SSLContext {
        +protocol: PROTOCOL_TLS_SERVER
        +certfile: str
        +keyfile: str
        +load_cert_chain()
        +wrap_socket()
    }
    
    class CertificateGenerator {
        +private_key: RSAPrivateKey
        +certificate: Certificate
        +subject_name: str
        +generate_private_key()
        +create_certificate()
        +save_to_files()
    }
    
    class WebInterface {
        +html_content: str
        +css_styles: str
        +javascript_logic: str
        +render_page()
        +handle_requests()
    }
    
    class FileHandler {
        +root_directory: str
        +serve_file()
        +get_content_type()
        +handle_404()
    }
    
    HTTPSServer --> SSLContext : uses
    HTTPSServer --> FileHandler : contains
    SSLContext --> CertificateGenerator : requires
    FileHandler --> WebInterface : serves
    
    note for HTTPSServer "Serveur HTTPS principal\navec support SSL/TLS"
    note for CertificateGenerator "Génère les certificats\nX.509 auto-signés"
    note for WebInterface "Interface utilisateur\nweb moderne"
```

## 📁 Structure du Projet

```
python-local-https/
├── 📂 Back-end/
│   └── 📓 main.ipynb              # Serveur HTTPS principal
├── 📂 Front-end/
│   ├── 📄 index.html              # Page web principale
│   ├── 🎨 style.css               # Styles CSS modernes
│   └── ⚡ script.js               # Logique JavaScript
├── 📂 certs-cryptography/
│   ├── 📓 cert_generator.ipynb    # Générateur de certificats
│   └── 📂 certs/
│       ├── 📜 certificate.pem     # Certificat public
│       └── 🗝️ private_key.pem     # Clé privée
├── 📂 certs-openSSL/
│   └── 🛠️ [Outils OpenSSL]
└── 📋 README.md                   # Documentation
```

## 🚀 Installation et Démarrage

### Prérequis
- Python 3.7+ 
- Jupyter Notebook/Lab
- Navigateur web moderne

### 1️⃣ Génération des Certificats

```bash
# Ouvrir le notebook de génération
jupyter notebook certs-cryptography/cert_generator.ipynb

# Exécuter toutes les cellules pour générer :
# - certificate.pem (certificat public)
# - private_key.pem (clé privée)
```

### 2️⃣ Lancement du Serveur

```bash
# Ouvrir le serveur principal
jupyter notebook Back-end/main.ipynb

# Exécuter les cellules dans l'ordre :
# 1. Import des bibliothèques
# 2. Configuration SSL
# 3. Lancement du serveur
```

### 3️⃣ Accès à l'Application

```
🌐 URL : https://localhost:4443
🔒 Protocole : HTTPS/TLS 1.3
📱 Compatible : Desktop & Mobile
```

## 🔐 Sécurité et SSL/TLS

### Implémentation Moderne

- **SSL Context** : Utilisation de `ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)`
- **Certificats X.509** : Auto-signés avec RSA 2048 bits
- **Chiffrement** : TLS 1.2/1.3 avec algorithmes sécurisés
- **Validation** : Gestion des erreurs de certificat

### Configuration SSL

```python
# Création du contexte SSL moderne
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(
    certfile="certs/certificate.pem",
    keyfile="certs/private_key.pem"
)

# Application au serveur
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)
```

## 🎨 Interface Utilisateur

### Design Features
- **Gradient Background** : Dégradé moderne bleu/noir
- **Glass Morphism** : Effet de verre avec transparence
- **Responsive Design** : Adaptation mobile/desktop
- **Animations** : Transitions fluides et feedback visuel

### Composants
- **Status Indicator** : Affichage en temps réel du statut
- **Request Button** : Bouton d'envoi de requêtes HTTPS
- **Response Display** : Zone d'affichage des réponses serveur

## 🧪 Tests et Validation

### Test de Connectivité
```javascript
// Test automatique de la connexion HTTPS
const testConnection = async () => {
    try {
        const response = await fetch('https://localhost:4443');
        console.log('✅ HTTPS Connection successful');
    } catch (error) {
        console.error('❌ HTTPS Connection failed:', error);
    }
};
```

### Validation du Certificat
- Vérification de la chaîne de certificats
- Test de la validité temporelle
- Contrôle de l'algorithme de signature

## 🛠️ Développement

### Personnalisation du Serveur
```python
# Modification du port
PORT = 8443  # Changez selon vos besoins

# Personnalisation du handler
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Logique personnalisée
        super().do_GET()
```

### Extension de l'Interface
- Ajout de nouvelles pages HTML
- Intégration d'APIs REST
- Implémentation de WebSockets sécurisés

## 📊 Monitoring et Logs

### Logs du Serveur
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('HTTPSServer')

# Logs automatiques des requêtes
logger.info(f"Request from {client_address}")
```

## 🔧 Dépannage

### Problèmes Courants

| Problème | Solution |
|----------|----------|
| `ssl.wrap_socket` deprecated | Utiliser `ssl.SSLContext` |
| Certificat non reconnu | Accepter l'exception dans le navigateur |
| Port déjà utilisé | Changer le PORT dans la configuration |
| Fichiers non trouvés | Vérifier les chemins relatifs |

### Commandes Utiles
```bash
# Vérifier les ports ouverts
netstat -an | findstr :4443

# Test SSL avec OpenSSL
openssl s_client -connect localhost:4443

# Validation du certificat
openssl x509 -in certificate.pem -text -noout
```

## 📚 Ressources et Références

- [RFC 2818 - HTTP Over TLS](https://tools.ietf.org/html/rfc2818)
- [Python SSL Documentation](https://docs.python.org/3/library/ssl.html)
- [X.509 Certificate Standards](https://tools.ietf.org/html/rfc5280)
- [TLS 1.3 Specification](https://tools.ietf.org/html/rfc8446)

## 🤝 Contribution

Les contributions sont les bienvenues ! Merci de :
1. Fork le projet
2. Créer une branche feature
3. Commit vos changements
4. Push vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

Développé avec ❤️ pour l'apprentissage de HTTPS et SSL/TLS en Python.

---

⭐ **N'hésitez pas à mettre une étoile si ce projet vous a été utile !**
