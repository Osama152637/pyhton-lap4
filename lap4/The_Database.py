import psycopg2
import sys

host = 'localhost'
user = 'omda2'
password = 'omda12'
dbname = 'iti'

def connect():
    try:
        connection = psycopg2.connect(host=host,user=user,password=password,dbname=dbname)
        return connection
    except Exception as e:
        print(f"Connection failed: {e}")
        sys.exit(1)

def selectfromtable(tablename):
    conn = connect()
    query = f'SELECT * FROM {tablename};'
    try:
        cur = conn.cursor()
        cur.execute(query)
        traineedata = cur.fetchall()
        return traineedata
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        conn.close()

def inserttrainee(id, name, age, track_name):
    conn = connect()
    query = "INSERT INTO trainee (id, name, age, track_name) VALUES (%s, %s, %s, %s);"
    try:
        cur = conn.cursor()
        cur.execute(query, (id, name, age, track_name))
        conn.commit()
        print("Insertion successful")
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        cur.close()
        conn.close()


def updatetrainee(id, name, age, track_name):
    conn = connect()
    query = f"UPDATE trainee SET name = '{name}', track_name = '{track_name}', age = {age} WHERE id = {id};"
    try:
        cur = conn.cursor()
        cur.execute(query, (name, track_name, id))
        conn.commit()
        print("Updatet successful")
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        conn.close()

def deletetrainee(id):
    conn = connect()
    query = "DELETE FROM trainee WHERE id = %s;"
    try:
        cur = conn.cursor()
        cur.execute(query, (id,))
        conn.commit()
        print("Deletion successful")
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        cur.close()
        conn.close()