from flask import Flask, render_template, abort

app = Flask(__name__)

# Use special @app.errorhandler() decorator for 404 errors.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# This one relates to app.route 500 below
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

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

# ...
@app.route('/500')
def error500():
    abort(500)