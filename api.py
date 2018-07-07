from flask import Flask

app = Flask('autocomplete')

@app.route('/ping/')
def ping():
    return 'pong!'


if __name__ == '__main__':
    app.run()
