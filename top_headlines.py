from flask import Flask, render_template
import nyt


app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name=nm, articals=nyt.top5)

if __name__ == '__main__':   
    app.run(debug=True)