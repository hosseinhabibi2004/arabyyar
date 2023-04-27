# External
from settings import __version__
from flask import render_template, request
from .numbers import arabic_calculator, number_to_arabic, clock, jalali2hijri
from .verb import arabic_verb, process_chapter, reverse_chapter


def index_view():
    response = {'version': __version__}
    return render_template('index.html', content = response)


def help_view():
    return render_template('help.html')


def arabic_calculator_view():
    math_string = request.args.get('mathString')
    if math_string != "":
        try:
            response = arabic_calculator(math_string)
        except:
            response = {
                "status": False,
                "result": {
                    "error": 201,
                    "math": math_string,
                }
            }
    else:
        response = {
            "status": False,
            "result": {
                "error": 201,
                "math": math_string,
            }
        }
    return render_template('calculator.html', content=response)


def number_to_arabic_view():
    number = request.args.get('number')
    if number != "":
        try:
            response = number_to_arabic(number)
        except:
            response = {
               "status": False,
                "result": {
                    "error": 201,
            }
        }
    else:
        response = {
            "status": False,
            "result": {
                "error": 201,
            }
        }
    return render_template('number.html', content=response)


def arabic_verb_view():
    word = request.args.get('w')
    future_type = request.args.get('f')
    pronoun = request.args.get('p')
    if word and future_type and pronoun:
        try:
            pronoun = int(pronoun)
            future_type = int(future_type)
            response = arabic_verb(word, future_type, pronoun)
        except:
            response = {
                'status': False,
                'result': {
                    'error': 201,
                    'word': None,
                    'future_type': None,
                    'pronoun': None,
                }
            }
    else:
        response = {
            'status': False,
            'result': {
                'error': 201,
                'word': None,
                'future_type': None,
                'pronoun': None,
            }
        }
    return render_template('verbs.html', content=response)


def chapters_view():
    base = request.args.get('base')
    chapter = request.args.get('chapter')
    pronoun = request.args.get('pronoun')
    if base and chapter and pronoun:
        try:
            chapter = int(chapter)
            pronoun = int(pronoun)
            response = process_chapter(base, chapter, pronoun)
        except:
            response = {
                "status": False,
                "result": {
                    "error": 201,
                    "base": base,
                    "chapter": chapter,
                    "pronoun": pronoun,
                    "past": None,
                    "present": None,
                    "impretive": None,
                    "infinitive": None,
                }
            }
    else:
        response = {
            "status": False,
            "result": {
                "error": 201,
                "base": base,
                "chapter": chapter,
                "pronoun": pronoun,
                "past": None,
                "present": None,
                "impretive": None,
                "infinitive": None,
            }
        }
    return render_template('chapter.html', content=response)


def detect_chapters_view():
    word = request.args.get('word')
    if word:
        try:
            response = response = reverse_chapter(word)
        except:
            response = {
                'status': False,
                'error': 201,
                'result': {
                    'pairs': {},
                    'word': word,
                }
            }
    else:
        response = {
            'status': False,
            'error': 201,
            'result': {
                'pairs': {},
                'word': word,
            }
        }
    return render_template('detect-chapters.html', content=response)


def calendar_view():
    jalali_year = request.args.get('y')
    jalali_month = request.args.get('m')
    jalali_day = request.args.get('d')
    if jalali_year and jalali_year and jalali_day:
        try:
            jalali_year = int(jalali_year)
            jalali_month = int(jalali_month)
            jalali_day = int(jalali_day)
            response = jalali2hijri(jalali_year, jalali_month, jalali_day)
        except:
            response = {
                "status": False,
                "result": {
                    "error": 201,
                    "jalali_year": jalali_year,
                    "jalali_month": jalali_month,
                    "jalali_day": jalali_day,
                }
            }
    else:
        response = {
            "status": False,
            "result": {
                "error": 201,
                "jalali_year": jalali_year,
                "jalali_month": jalali_month,
                "jalali_day": jalali_day,
            }
        }
    return render_template('calendar.html', content=response)

    
def clock_view():
    hrs = request.args.get('hrs')
    mns = request.args.get('mns')
    mode = request.args.get('mode')
    if hrs and mns and mode:
        try:
            hrs = int(hrs)
            mns = int(mns)
            mode = True if mode == '1' else False
            response = clock(hrs, mns, mode)
        except:
            response = {
                "status": False,
                "result": {
                    "error": 201,
                    "hour": None,
                    "minute": None,
                    "mode": None,
                }
            }
    else:
        response = {
            "status": False,
            "result": {
                "error": 201,
                "hour": None,
                "minute": None,
                "mode": None,
            }
        }
    return render_template('clock.html', content=response)


def color_view():
    return render_template('color.html')
