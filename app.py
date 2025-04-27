from flask import Flask, send_from_directory, request, jsonify
import re
import requests

app = Flask(__name__)

SUSPICIOUS_KEYWORDS = [
    'login', 'verify', 'update', 'secure', 'account', 'bank', 'webscr', 'ebayisapi', 'paypal',
    'security', 'confirm', 'signin', 'wp-', 'admin', 'password', 'reset', 'validate', 'unsubscribe'
]

def detect_phishing(url):
    if re.search(r'http[s]?://(\d{1,3}\.){3}\d{1,3}', url):
        return True, 'L’URL contient une adresse IP (signe courant de phishing).'
    for kw in SUSPICIOUS_KEYWORDS:
        if kw in url.lower():
            return True, f"Mot-clé suspect détecté dans l’URL : '{kw}'"
    if url.count('.') > 3:
        return True, 'Trop de sous-domaines dans l’URL.'
    
    try:
        resp = requests.get(f'https://checkurl.phishtank.com/checkurl/index.php?url={url}', timeout=3)
        if 'phish_detail_page' in resp.text:
            return True, 'URL détectée comme phishing par PhishTank.'
    except Exception:
        pass
    return False, 'Aucun signe de phishing détecté.'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

import urllib.parse

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url', '')
    # Vérification que c'est bien une URL (commence par http:// ou https://)
    if not (url.startswith('http://') or url.startswith('https://')):
        return jsonify({'error': 'Merci de fournir une URL commençant par http:// ou https://'}), 400
    is_phish, reason = detect_phishing(url)
    return jsonify({'phishing': is_phish, 'reason': reason})

if __name__ == '__main__':
    app.run(debug=True)
