from flask import url_for


def test_ping(client):
    response = client.get(url_for('ping'))
    assert response.status_code == 200
    assert response.get_data() == b'pong!'
