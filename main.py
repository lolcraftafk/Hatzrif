from flask import Flask, render_template
from markupsafe import Markup
import json

app = Flask(__name__)


@app.route('/')
def index():
    file = open("static/timetables.json", "r", encoding="utf-8")
    text = file.read()
    table = json.loads(text)
    return render_template('timetable.html', sunday=table['sunday'], monday=table['monday'], tuesday=table['tuesday'], wednesday=table['wednesday'], thursday = table['thursday'], markup=Markup)

app.run(debug=True)