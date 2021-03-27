from flask import *
from Backends import *
from flask_mysqldb import MySQL
import numpy as np

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


@app.route('/login', methods=['POST'])
def post_page_login():
    if request.method == 'POST':
        user = request.form['username']
        return "your username is : "+str(user)


@app.route('/login')
def get_page_login():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    
    
    data = cur.fetchall()
    data = np.asarray(data)
    
    print(data)

    cur.close()

    

    return render_template("admin/login.html")



# Admin
@app.route(route_admin) # /admin
def get_page_admin():

    return render_template("admin/index.html")


# Receptionist


if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)
