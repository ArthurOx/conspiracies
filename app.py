from flask import Flask
from flask import request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/conspiracy', methods=['GET'])
def get_conspiracy():
    prompt = request.args.get('question')
    return prompt


if __name__ == '__main__':
    app.run(debug=True)
