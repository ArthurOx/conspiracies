import json

from flask import Flask
from flask import request
from main import few_shot_completion
app = Flask(__name__)
# secret = 'f05f835eb2e7463f800060e42ac5111e'
# app.secret_key = secret
@app.route('/')
def hello_world():
    return 'Hello! World!'


@app.route('/conspiracy')
def get_conspiracy():
    question = request.args['prompt']
    argument = few_shot_completion(question)['choices'][0]['text']
    print(argument)
    answer = {'answer': argument}
    return app.response_class(response=json.dumps(answer), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
