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
# Use app.logger to log errors.
# app.logger.debug(): For detailed information about the event.
# app.logger.info(): Confirmation that things are working as expected.
# app.logger.warning(): Indication that something unexpected happened (such as “disk space low”), but the application is working as expected.
# app.logger.error(): An error occurred in some part of the application.
# app.logger.critical(): A critical error; the entire application might stop working.
@app.route('/messages/<int:idx>')
# define three messages.
def message(idx):
    # log event that is working as expected with info
    app.logger.info('Building the messages list...')
    messages = ['Message Zero', 'Message One', 'Message Two']
    try:
        # detailed info with debug level
        app.logger.debug('Get message with index: {}'.format(idx))
        return render_template('message.html', message=messages[idx])
    except IndexError:
        # log index number of error
        app.logger.error('Index {} is causing an IndexError'.format(idx))
        abort(404)

@app.route('/500')
def error500():
    abort(500)