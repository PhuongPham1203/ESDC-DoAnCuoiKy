from flask import *
from flask_mysqldb import MySQL
import numpy as np
import string,random

def checktoken(request_page,mysql):
    
    id_user = 0
    username_user = ""
    token_user = ""
    level = 0
    isTrue = False
    rep = ""
    if('token' in request_page):

        query = "SELECT * FROM user WHERE token=%s AND status_check=1"
        cur = mysql.connection.cursor()
        cur.execute(query,(request_page.get('token'),))
        
        data = cur.fetchall()
        data = np.asarray(data)
        cur.close()

        if(len(data)>0):
            #print(data[0])
            isTrue = True
            id_user = data[0][0]
            username_user = data[0][1]
            token_user = data[0][3]
            level = data[0][4]
        else:
            rep = make_response(redirect("/login"))
            rep.set_cookie('token', '', expires=0)
            isTrue = False
            return isTrue,rep,id_user,username_user,token_user,level


    return isTrue,rep,id_user,username_user,token_user,level