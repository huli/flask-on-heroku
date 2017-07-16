import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/<nameparameter>')
def halloWeltAusgeben(nameparameter=None):
    return render_template('index.html', name=nameparameter)


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
