from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World !!'


@app.route('/sample', methods=['POST'])
def sample_post():
    return "param1:{}".format(request.form['param1'])


@app.route('/sample_get', methods=['GET'])
def sample_get():
    param = request.args.get('param1')
    return "param1:{}".format(param)


app.run(host="0.0.0.0", port=5000, debug=True)
