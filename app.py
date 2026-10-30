import os

from flask import Flask, render_template_string

app = Flask(__name__)

BASE_STYLE = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #eef2f7;
        text-align: center;
        padding: 50px 15px;
    }
    .container {
        max-width: 650px;
        margin: auto;
        background: white;
        padding: 30px;
        border-radius: 12px;
    }
    h1 {
        color: #2457a7;
    }
    p {
        font-size: 18px;
        line-height: 1.6;
    }
    a {
        color: #2457a7;
        text-decoration: none;
        font-weight: bold;
    }
</style>
"""

HOME_PAGE = """
<!DOCTYPE html>
<html lang="kk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PaaS веб-қосымшасы</title>
    """ + BASE_STYLE + """
</head>
<body>
    <div class="container">
        <h1>PaaS платформасындағы веб-қосымша</h1>
        <p>Бұл қосымша Python және Flask көмегімен әзірленген және
        бұлттық PaaS платформасына орналастыруға дайын.</p>
        <p><a href="/info">Қосымша туралы ақпарат</a></p>
    </div>
</body>
</html>
"""

INFO_PAGE = """
<!DOCTYPE html>
<html lang="kk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Қосымша туралы</title>
    """ + BASE_STYLE + """
</head>
<body>
    <div class="container">
        <h1>Қосымша туралы ақпарат</h1>
        <p><b>Тақырып:</b> PaaS платформасында қарапайым веб-қосымшаны әзірлеу</p>
        <p><b>Технологиялар:</b> Python, Flask, HTML, CSS</p>
        <p><b>Платформа үлгісі:</b> PaaS (Platform as a Service)</p>
        <p><a href="/">Басты бетке оралу</a></p>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HOME_PAGE)


@app.route("/info")
def info():
    return render_template_string(INFO_PAGE)


if __name__ == "__main__":
    # PaaS платформалары портты PORT айнымалысы арқылы береді
    port = int(os.environ.get("PORT", 5000))
    # debug тек жергілікті ортада қосылады (FLASK_DEBUG=1 болса)
    debug = os.environ.get("FLASK_DEBUG", "1" if "PORT" not in os.environ else "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
