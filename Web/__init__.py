from flask import Flask
from Web.views import (
    index_view,
    help_view,
    clock_view,
    arabic_calculator_view,
    number_to_arabic_view,
    detect_chapters_view,
    chapters_view,
    color_view,
    arabic_verb_view,
    calendar_view,
)
import logging
import settings

app = Flask(__name__, template_folder=settings.Web_Template_Folder, static_folder=settings.Web_Static_Folder)
app.debug = False

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
app.add_url_rule('/dchapters', 'detect_chapters_view', view_func=detect_chapters_view, methods=['GET'])
app.add_url_rule('/calendar', 'calendar', view_func=calendar_view, methods=['GET'])


def run_flask():
    app.run(port=9000)
