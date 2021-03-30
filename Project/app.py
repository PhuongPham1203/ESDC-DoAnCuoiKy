from flask import *
from Backends import token
from flask_mysqldb import MySQL
import numpy as np
import string,random

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'esdc_doan'

mysql = MySQL(app)

route_admin = "/admin"  # admin
route_receptionist = "/receptionist"  # le tan

level_admin = 1
level_letan = 2

# Hotel


@app.route('/')
def hello_world():
    return render_template("hotel/index.html")


@app.route('/main')
def main_web():
    return 'Đây là kết quả khi chạy gọi localhost:9000/main'

# Login
def token_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route('/login', methods=['POST'])
def post_page_login():
    if request.method == 'POST':
        if(('username' in request.form) and ('password' in request.form)):

            us = request.form['username']
            pa = request.form['password']

            cur = mysql.connection.cursor()
            query = "SELECT * FROM user WHERE username=%s AND password=%s AND status_check = 1"
            cur.execute( query,(us,pa,) )
            
            data = cur.fetchall()
            data = np.asarray(data)
            cur.close()
            if(len(data)>0):
                print(data[0])
                id_user = data[0][0]
                token = token_generator()
                # set token to database
                query = "UPDATE user SET token=%s WHERE id="+str(id_user)
                cur = mysql.connection.cursor()
                cur.execute( query,(token,) )
                mysql.connection.commit()
                
                cur.close()
                
                rep = make_response(redirect(route_admin))

                rep.set_cookie('token', token)
                return rep
            
    return get_page_login()


@app.route('/login')
def get_page_login():

    """
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    
    
    data = cur.fetchall()
    data = np.asarray(data)
    
    
    #print(data)

    cur.close()
    """
    return render_template("admin/login.html")

@app.route('/logout')
def get_page_logout():
    rep = make_response(redirect("/login"))

    if('token' in request.cookies):
        rep.set_cookie('token', '', expires=0)

    return rep

# Admin
@app.route(route_admin) # /admin
def get_page_admin():
    #print(request.cookies.get('token'))
    isTrue,rep,id_user,username_user,token_user,level = token.checktoken(request.cookies,mysql)

    if(isTrue):
        print(username_user+" "+token_user+" "+str(level))

        data = {"username":username_user,
                "level":level}

        if(level==level_admin):
            pass
    else:
        return rep
    

    return render_template("admin/index.html",data=data)


# Receptionist

if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)
