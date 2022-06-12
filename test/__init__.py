from pydoc import render_doc
from turtle import title
from urllib import response
from flask import Flask, render_template
from flask import g
from flask import request, Response, make_response
from flask import session
from datetime import date, datetime, timedelta
from test.init_db import init_database, db_session


app = Flask(__name__)


app.debug = True        # use only debug

app.config.update(
    SECRET_KEY='X1243yRH!mMwf',
    SESSION_COOKIE_NAME='pyweb_flask_session',
    PERMANEMT_SESSION_LIFETIME=timedelta(31)
)

#set cookie
@app.route("/dc")
def dc():
    key = request.args.get("key")
    val = request.args.get("val")
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    return make_response(res)


#set session
@app.route("/setsess")
def setsess():
    session['Token'] = "yongchul"
    return "sesssion 설정되었습니다"

#get session
@app.route("/getsess")
def getsess():
    return session.get('Token')

#delete session
@app.route("/delsess")
def delsess():
    if session['Token'] :
        del session['Token']
    return "session 삭제되었습니다."



@app.route("/")
def helloWorld():
    return render_template("default.html", title="Yongchul")

@app.route("/laser")
def laser():
    return render_template("laser.html")

@app.route("/db_conn")
def db_conn():
    return render_template("init_db.py")
    
@app.before_first_request
def beforeFirstRequest():
    print("before firest request!")
    init_database()

@app.after_request
def afterReques():
    print('after request!')

@app.teardown_request
def teardownRequest(exception):
    print("teardown_request!! >>", exception)

@app.teardown_appcontext
def teardown_appcontext(exception):
    print(">>>  teardown appcontext!! >>", exception)
    db_session.remove()