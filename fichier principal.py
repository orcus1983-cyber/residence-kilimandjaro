from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bienvenue à la Résidence Kilimandjaro !'

if __name__ == '__main__':
    app.run(debug=True)
