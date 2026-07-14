from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Ciao da Render! L'app Python è online."

if __name__ == '__main__':
    app.run()
