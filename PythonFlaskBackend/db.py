import psycopg2


conn = psycopg2.connect(host="localhost",database="carparking",user="postgres",password="3255")
cur= conn.cursor()