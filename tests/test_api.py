from flask import url_for

import api
from trie import Trie


def test_ping(client):
    response = client.get(url_for('ping'))
    assert response.status_code == 200
    assert response.get_data() == b'pong!'


def test_should_autocomplete_return_an_empty_list(client):
    response = client.get(
        url_for('autocomplete'),
        query_string={'q': ''})
    assert response.status_code == 200
    assert response.json['options'] == []


def test_should_autocomplete(client):
    trie = Trie()
    trie.insert_words(['Facebook', 'Facebook Lite', 'Faca'])
    api.trie = trie
    response = client.get(
        url_for('autocomplete'),
        query_string={'q': 'face'})
    assert response.status_code == 200
    assert response.json['options'] == ['Facebook', 'Facebook Lite']


def test_should_autocomplete_return_all_options_with_empty_query(client):
    words = ['foo', 'bar', 'buzz']
    trie = Trie()
    trie.insert_words(words)
    api.trie = trie
    response = client.get(
        url_for('autocomplete'),
        query_string={'q': ''})
    assert response.status_code == 200
    assert response.json['options'] == words
