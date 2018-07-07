from flask import Flask, request, jsonify

from trie import Trie
from utils import Timer


app = Flask('autocomplete')
app.config['ENV'] = 'development'
app.config['TESTING'] = True

trie = Trie()


@app.route('/ping/', methods=['GET'])
def ping():
    return 'pong!'


@app.route('/autocomplete/', methods=['GET'])
def autocomplete():
    query = request.args.get('q', '')
    timer = Timer()
    with timer:
        items = trie.iterwords(prefix=query)
    response = {
        'options': list(items),
        'response_time': timer.result,
    }
    return jsonify(response), 200
