from Web import run_flask

if __name__ == '__main__':
    run_flask()

from flask import Flask
from Apps.views import (
    index_view,
    help_view,
    clock_view,
    arabic_calculator_view,
    number_to_arabic_view,
    chapters_view,
    color_view,
    arabic_verb_view,
)
import webbrowser
import logging
import sys
import subprocess
from Apps.printer import printer


# if getattr(sys, 'frozen', False):
#     template_folder = '\\'.join((sys._MEIPASS.replace('/', '\\'), 'media/templates'.replace('/', '\\'), ))
#     static_folder = '\\'.join((sys._MEIPASS.replace('/', '\\'), 'media/static'.replace('/', '\\'), ))
#     app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
# else:
#     app = Flask(__name__)

app = Flask(__name__, template_folder='media/templates/', static_folder='media/static/')

log = logging.getLogger('werkzeug')
log.disabled = True

app.add_url_rule('/', 'index', view_func=index_view, methods=['GET'])
app.add_url_rule('/help', 'help', view_func=help_view, methods=['GET'])
app.add_url_rule('/calculator', 'calculator', view_func=arabic_calculator_view, methods=['GET'])
app.add_url_rule('/chapters', 'chapters', view_func=chapters_view, methods=['GET'])
app.add_url_rule('/color', 'color', view_func=color_view, methods=['GET'])
app.add_url_rule('/nta', 'nta', view_func=number_to_arabic_view, methods=['GET'])
app.add_url_rule('/verbs', 'verbs', view_func=arabic_verb_view, methods=['GET'])
app.add_url_rule('/clock', 'clock', view_func=clock_view, methods=['GET'])


if __name__ == '__main__':
    app.debug = False
    main()
    webbrowser.open('http://127.0.0.1:9000/')
    app.run(port=9000)