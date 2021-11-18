from flask import Flask, render_template
import math

from werkzeug.utils import redirect

app = Flask(__name__)


# Routes here:
@app.route('/')
def index(y = 8, x = 8):
    color_1 = 'red'
    color_2 = 'black'
    x = int(x/2)
    y = int(y/2)
    return render_template('index.html', x = x, y = y, color_1 = color_1, color_2 = color_2)


@app.route('/<int:y>')
def check_x(y, x = 8):
    color_1 = 'red'
    color_2 = 'black'
    x = int(x/2)
    y = int(y/2)
    return render_template('index.html', x = x, y = y, color_1 = color_1, color_2 = color_2)

@app.route('/<int:x>/<int:y>')
def check_x_y(x, y):
    color_1 = 'red'
    color_2 = 'black'
    x = int(x/2)
    y = int(y/2)
    return render_template('index.html', x = x, y = y, color_1 = color_1, color_2 = color_2)

@app.route('/<int:x>/<int:y>/<color_1>')
def color_1(x, y, color_1):
    color_2 = 'black'
    x = int(x/2)
    y = int(y/2)
    return render_template('index.html', x = x, y = y, color_1 = color_1, color_2 = color_2)

@app.route('/<int:x>/<int:y>/<color_1>/<color_2>')
def color_2(x, y, color_1, color_2):
    x = int(x/2)
    y = int(y/2)
    return render_template('index.html', x = x, y = y, color_1 = color_1, color_2 = color_2)




if __name__ =="__main__":
    app.run(debug=True)