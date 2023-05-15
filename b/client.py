import requests

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    response = requests.get('http://container_a:8080')
    return f'Hello from Container B! World from Container A: {response.text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
