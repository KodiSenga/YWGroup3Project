from pymongo import *
from datetime import *
from random import *

def openConnection():
    host = 'localhost'
    port = 27017

    conn = MongoClient(host,port)

    return conn

def closeConnection(conn):
    conn.close()