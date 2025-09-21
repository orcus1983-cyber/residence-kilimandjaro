from flask import Flask, render_template

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route pour la page d'accueil
@app.route('/')
def index():
    # Utiliser le template 'index.html' qui est dans le dossier 'templates'
    return render_template('index.html')

# Lancer l'application si ce fichier est exécuté directement
if __name__ == '__main__':
    app.run(debug=True)
