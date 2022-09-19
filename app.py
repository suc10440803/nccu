from flask import Flask
from flask.templating import render_template
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def redir():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()