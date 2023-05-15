from flask import Flask

app = Flask(__name__)

print('App started successfully')

@app.route('/')
def hello():
    print('Received a request to the root URL')
    return 'World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
