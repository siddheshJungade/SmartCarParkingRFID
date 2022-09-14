from flask import jsonify
from flask import make_response,redirect,url_for
from app import app,obj,off,socketio,reader
from controller.carparking import start_system
import RPi.GPIO as GPIO
from threading import Thread
import time



@app.route('/')
def home():
    response = make_response("Smart Car Parking System",200)
    response.mimetype = "text/plain"
    return response

@app.route('/start-sys',methods=["POST", "GET"])
def startSys():
    global off
    print(off)
    if off == 1:
        off = 2
        status = Thread(target=start_system(),name="start-app")
        status.setDaemon(True)
        status.start()
        response = "Smart Car Parking System"
    else:
        response = "Code is already runing in thread"
    return response


@app.route('/recharge')
def recharge():
    global off
    id = reader.read_id()
    socketio.emit('message','recharge')
    obj.recharge_tag(id)
    socketio.emit('message','Recharge Done')
    off = 1
    return redirect(url_for('startSys'))

@app.route('/no-recharge')
def norecharge():
    global off
    off = 1
    return redirect(url_for('startSys'))

@app.route('/active-tags')
def get_active_tag_controller():
    res = obj.get_active_tags()
    coloum = ('user_id','balance')
    results = []
    for row in res:
        results.append(dict(zip(coloum, row)))
    return jsonify(results)


@app.route('/cars-history')
def get_cars_history_controller():
    res = obj.get_cars_history()
    coloum = ('user_id','intime','outtime','duration')
    results = []
    for row in res:
        results.append(dict(zip(coloum, row)))
    return jsonify(results)

    

