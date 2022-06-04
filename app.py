from flask import Flask, render_template

app = Flask(__name__)

# There are two errors in this code: 
# 1. did not import the render_template() function
# 2. index.html template file does not exist.
@app.route('/')
def index():
    return render_template('index.html')