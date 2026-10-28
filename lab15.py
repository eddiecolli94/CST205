from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)

# task 2
@app.route('/')
def hello():
    return """
    <p>John: LOL (Laugh Out Loud)</p>
    <p>Jane: ASAP (As Soon As Possible)</p>
    <p>Jimmy: GNU (GNU Not Linux)</p>
    """

# task 3
@app.route('/edward')
def t_test():
    return render_template('template.html', acronym='FTL (Faster Than Light)')

# task 4
bootstrap = Bootstrap5(app)
@app.route('/image')
def image():
    return render_template('image.html')