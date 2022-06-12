from test import app

@app.route("/test")
def test ():
    return "test"