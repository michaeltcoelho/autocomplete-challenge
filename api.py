import time

from flask import Flask, request, jsonify

from trie import Trie

app = Flask('autocomplete')

trie = Trie()


@app.route('/ping/', methods=['GET'])
def ping():
    return 'pong!'


@app.route('/autocomplete/', methods=['GET'])
def autocomplete():
    query = request.args.get('q', '')
    start = time.perf_counter()
    words = list(trie.iterwords(prefix=query))
    end = time.perf_counter() - start
    response = {
        'options': words,
        'time': f'It took {end:.8f} seconds',
    }
    return jsonify(response), 200
