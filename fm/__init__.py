from urllib import response
from flask import Flask
from flask import render_template
from fm.init_db import init_database, db_session

from datetime import timedelta


app = Flask(__name__)
import fm.views
import fm.db_models
import fm.reg_models


app.debug = True        # use only debug

app.config.update(
    SECRET_KEY='X1243yRH!mMwf',
    SESSION_COOKIE_NAME='pyweb_flask_session',
    PERMANEMT_SESSION_LIFETIME=timedelta(31)
)


@app.route("/ts")
def helloWorld():
    return render_template("laser_success.html", title="Yongchul")

@app.before_first_request
def beforeFirstRequest():
    print("before firest request!")
 #   init_database()

@app.after_request
def afterRequest(response):
    print('after request!')
    return response

@app.teardown_request
def teardownRequest(exception):
    print("teardown_request!! >>", exception)

@app.teardown_appcontext
def teardown_appcontext(exception):
    print(">>>  teardown appcontext!! >>", exception)
    db_session.remove()