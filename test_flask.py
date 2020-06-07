from flask import Flask
app = Flask(__name__)

@app.route('/test')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run('0.0.0.0', 8810)
