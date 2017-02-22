from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Homepage here!'

@app.route('/about/')
def about():
    return 'About content go here!'

if __name__ == '__main__':
    app.run(debug = True)
