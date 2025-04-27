# Détecteur de Phishing

Bienvenue sur mon projet de Détecteur de Phishing !

## Pourquoi ce projet ?

Je m’appelle Jordan Lengrai, et j’ai créé cette application web parce que je voulais un outil simple, efficace et sympa pour repérer les liens suspects (et accessoirement, montrer que je sais coder un peu plus qu’un simple "Hello World").

Que tu sois curieux, prudent, ou que tu veuilles juste tester des liens douteux envoyés par ton oncle, cette appli est faite pour toi !

## Ce que tu peux faire avec
- Coller une URL ou un email et savoir tout de suite si ça sent le poisson (phishing) ou si c’est clean
- Profiter d’une interface moderne, colorée, et responsive (ça marche aussi sur ton téléphone !)
- Voir le résultat affiché clairement, avec des couleurs et des icônes (parce que le rouge et le vert, c’est plus parlant)

## Comment ça marche ?
- L’appli regarde la structure du lien (présence d’IP, sous-domaines bizarres, mots-clés suspects…)
- Elle interroge aussi la base publique PhishTank pour voir si l’URL est déjà connue comme dangereuse
- Le tout, sans prise de tête et sans jargon technique

## Installation rapide
1. Clone ce dépôt :
```bash
git clone <url_du_repo>
cd DetecteurPishin
```
2. Installe les dépendances Python :
```bash
pip install -r requirements.txt
```
3. Lance l’appli :
```bash
python app.py
```
4. Va sur [http://127.0.0.1:5000](http://127.0.0.1:5000) et amuse-toi !

## Pour aller plus loin
- Tu veux changer les couleurs ou les textes ? Va dans `static/style.css` ou `templates/index.html`.
- Tu veux ajouter tes propres règles de détection ? Modifie la fonction `detect_phishing` dans `app.py`.
- Tu as une idée d’amélioration ou tu as trouvé un bug ? N’hésite pas à me contacter ou à faire une pull request !

---

**Jordan Lengrai**
# DetecteurPishing
