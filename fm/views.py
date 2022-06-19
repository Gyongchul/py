from flask import redirect, render_template
from fm import app
from fm.init_db import db_session
from sqlalchemy.exc import SQLAlchemyError
from flask_wtf import FlaskForm
from fm.db_models import Laser
from fm.reg_models import regLaserForm


@app.route('/')
def hellofm():
   return render_template("default.html")


@app.route('/laserForm')
def laserForm():
   try:
      lsr = Laser("part_id","part_name","youben","NTC", 1, 2)
#      db_session.add(lsr)
#      db_session.commit()
      print("sussess insert ===================================================")
   except SQLAlchemyError as sqlerror:
      db_session.rollback()
      print("sqlError==============================================================", sqlerror)
   except:
      print("Error")

   return render_template("/laserFormSuccess")

@app.route('/laserFormSuccess')
def laserFormSuccess():
   return render_template("laser_success.html")

@app.route("/laser")
def laser():
   form = regLaserForm()
   if form.validate_on_submit():
      laser_mechine = form.laser_mechine.data
      laser_project = form.laser_project.data
      laser_partNo = form.laser_partNo.data
      laser_worker = form.laser_worker
      laser_qty = form.laser_qty
      laser_devictive = form.laser_defective
      return redirect('laserFormSuccess')

   return render_template("laser.html", form = form)

@app.route("/dbconn")
def dbconn():
    return "Hi dbconn"
