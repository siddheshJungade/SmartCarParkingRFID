# from controller.lcd import lcd
import time
import math
from datetime import datetime
from controller.moter import moters, config
from app import obj, start,reader,counter,counterIN,counterOut,socketio,off
from controller.rechargeTag import rechargeTag






def carOut(id,balance_in_Tag):
    global counter
    global counterOut
    outTime = str(datetime.now().time().replace(microsecond=0))
    toupleofIdINStart = list(start.get(id))
    finishTime = time.perf_counter() - toupleofIdINStart[0]
    FinishTimeSec = math.floor(finishTime)
    amount = math.floor((FinishTimeSec/60))*10 + 10
    print(FinishTimeSec, FinishTimeSec/60, FinishTimeSec % 60)
    print(math.floor(FinishTimeSec/60), " : ", round(FinishTimeSec %60), ' Min ', amount, ' Rs')
    # lcd.message('Amount Rs:'+str(amount)+" Rs")
    socketio.emit('message',f'Amount Rs: {str(amount)} Rs')
    time.sleep(2)
    counter -= 1
    print('Previous Balance in card :',balance_in_Tag)
    balance_in_Tag = balance_in_Tag-amount
    print(balance_in_Tag, id, toupleofIdINStart[1], outTime, FinishTimeSec)
    obj.add_into_history(id, toupleofIdINStart[1], outTime, FinishTimeSec)
    print("history done")
    obj.update_tag_balance(id, balance_in_Tag)
    print(outTime)
    counter -= 1
    counterOut += 1  
    amountTime = '\nTime:'+str(math.floor(FinishTimeSec/60))+":" + str(round(FinishTimeSec%60,0))+" Min"
    socketio.emit('message',amountTime)
    del start[id]
    time.sleep(2)
    if(balance_in_Tag <= 0):
        obj.delete_car_balance(id)        
        rechargeTag(id)
    moters(2)


def carIn(id):
    global counter
    global counterIN
    inTime = str(datetime.now().time().replace(microsecond=0))
    print(inTime)
    timeIn = time.perf_counter()
    print(time)
    start.update({id: [timeIn, inTime]})
    print(start)
    counter += 1
    counterIN += 1 
    moters(1)

def recharge(id):
        print('Insufficient\n....Balance....')
        socketio.emit('message',f"Insufficient\n....Balance....")
        time.sleep(2)
        print("Please recharge")
        socketio.emit('message',"recharge")
        return 


def start_system():
    global off
    try:
        while True :
            print("Smart parking System")
            socketio.emit('message',"Smart Carparking System is Running")
            time.sleep(3)
            print(start)
            print("------------------------------Welcome Please Tab Card---------------------------------------------------")
            socketio.emit('message',"Welcome Please Tab Card")
            id = reader.read_id()

            print(id)
  
            tagPresent = obj.get_single_tag_balance(id)
            if tagPresent != None:
                balance_in_tag = tagPresent[0]
                print("Access Granted")
                socketio.emit('message',"Access Granted")
                time.sleep(2)
                if id not in start.keys():
                    carIn(id)
                    print("Total Car In :",counterIN)
                    socketio.emit('message',f"Total Car : {counterIN}")
                else:
                    carOut(id,balance_in_tag)
                    print("Total Car Out :",counterOut)
                    socketio.emit('message',f"Total Car Out : {counterOut}")
                time.sleep(2)
            else:
                recharge(id)
                off = 1
                return 
            time.sleep(1)
            

    
    except KeyboardInterrupt:
                print("Code Exit ....")
                time.sleep(2)
                obj.close_connection()
        
