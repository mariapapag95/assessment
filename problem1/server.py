from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message':'hello'})

@app.route('/sum', methods=['GET','POST'])
def the_sum():
    num_list = [1,2,3,4,5]
    the_sum = sum(num_list)
    if request.method == 'GET':
        return jsonify({'sum':the_sum})
    elif request.method == 'POST':
        return jsonify({'values':num_list})

if __name__ == '__main__':
    app.run(port = 3333, debug = True)