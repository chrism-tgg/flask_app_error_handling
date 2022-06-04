from flask import Flask, render_template, abort

app = Flask(__name__)

# There are two errors in this code: 
# 1. did not import the render_template() function
# 2. index.html template file does not exist.
@app.route('/')
def index():
    return render_template('index.html')

# URL variable idx to determine where messages will be displayed
@app.route('/messages/<int:idx>')
# define three messages.
def message(idx):
    messages = ['Message Zero', 'Message One', 'Message Two']
    # Error handling with try...except clause
    try:
        return render_template('message.html', message=messages[idx])
    except IndexError:
        abort(404)