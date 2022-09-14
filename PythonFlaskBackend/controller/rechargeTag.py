from app import obj,socketio


def rechargeTag(id=0):
    socketio.emit('message','recharge')
    rec = input('Recharge Yes NO :')
    print(rec)
    if rec == "y":
        obj.recharge_tag(id)
    socketio.emit('message','Recharge Done')
