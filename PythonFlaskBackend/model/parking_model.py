import psycopg2
from db import *

class Parking_model():
    def __init__(self):
        self.conn = conn
        self.cur = cur

    def get_active_tags(self):
        self.cur.execute("SELECT * FROM car_balance")
        result = self.cur.fetchall()
        return result
    
    def get_single_tag_balance(self,id):
        self.cur.execute("SELECT balance FROM car_balance WHERE user_id=%s;" %id)
        self.conn.commit()
        balance_in_tuple = self.cur.fetchone()
        return balance_in_tuple
    
    def recharge_tag(self,id):
        self.cur.execute("INSERT INTO car_balance (user_id,balance) VALUES (%s,%s);" %(id,100))
        self.conn.commit()

    def update_tag_balance(self,id,balance_in_table):
        self.cur.execute("UPDATE car_balance SET balance=%s WHERE user_id=%s;" %(balance_in_table,id))
        self.conn.commit()

    def delete_car_balance(self,id):
        self.cur.execute("DELETE FROM car_balance WHERE user_id=%s;" %id)
        self.conn.commit()
    


    def get_cars_history(self):
        self.cur.execute("SELECT * FROM cars_history")
        result = self.cur.fetchall()
        print(result)
        return result

    
    def add_into_history(self,id,inTime,outTime,sec):
        self.cur.execute("INSERT INTO cars_history(user_id,intime,outtime,duration) VALUES (%s,'%s','%s',%s);" %(id,inTime,outTime,sec))
        self.conn.commit()


    def close_connection(self):
        self.cun.close()