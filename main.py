from flask import Flask, render_template
from markupsafe import Markup


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('timetable.html', sunday=[Markup("<b>מד\"צים ז' - אופק </b></br> (17:00-18:00)"), Markup("<b>מרחב פתוח</b></br> (16:00-21:00)")])

app.run(debug=True)