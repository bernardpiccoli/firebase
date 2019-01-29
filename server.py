from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None ):
    if(name is None):
        name="Valdinei"
    
    return render_template('hello.html', name=name)

#FLASK_APP=server.py flask run