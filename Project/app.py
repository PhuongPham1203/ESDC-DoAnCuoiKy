from flask import *
from Backends import token
from flask_mysqldb import MySQL
import numpy as np
import string
import random


def token_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


app = Flask(__name__)
app.secret_key = token_generator()


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
        if(('username' in request.form) and ('password' in request.form)):

            us = request.form['username']
            pa = request.form['password']

            cur = mysql.connection.cursor()
            query = "SELECT * FROM user WHERE username=%s AND password=%s AND status_check = 1"
            cur.execute(query, (us, pa,))

            data = cur.fetchall()
            data = np.asarray(data)
            cur.close()
            if(len(data) > 0):
                # print(data[0])
                id_user = data[0][0]
                token = token_generator()
                # set token to database
                query = "UPDATE user SET token=%s WHERE id="+str(id_user)
                cur = mysql.connection.cursor()
                cur.execute(query, (token,))
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
        session.pop('username', None)
        session.pop('id', None)
        session.pop('level', None)
        rep.set_cookie('token', '', expires=0)

    return rep

# ! Admin


@app.route(route_admin)  # /admin
def get_page_admin():
    # print(request.cookies.get('token'))
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue):
        #print(username_user+" "+token_user+" "+str(level))
        session['username'] = username_user
        session['id'] = id_user
        session['level'] = level

        data = {"username": username_user,
                "level": level}

        if(level == level_admin):
            pass
    else:
        return rep

    return render_template("admin/index.html", data=data)


# * Kiểu phòng
@app.route("/kieuphong")  # /kieuphong
def get_page_kieuphong():
    # print(request.cookies.get('token'))
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM room_type WHERE status_check = 1")

        data2 = cur.fetchall()
        data2 = np.asarray(data2)

        # print(data2)

        cur.close()

    else:
        return rep

    return render_template("admin/kieuphong.html", data=data, data2=data2)


@app.route("/addkieuphong", methods=['POST'])  # /addkieuphong
def get_page_addkieuphong():
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}

        if request.method == 'POST':
            if(('nameroom' in request.form) and ('numbera' in request.form) and ('numberc' in request.form) and ('description' in request.form)):
                query = "INSERT INTO room_type (name,description,number_adult,number_children) VALUES (%s, %s, "+str(
                    request.form["numbera"])+","+str(request.form["numberc"])+")"
                cur = mysql.connection.cursor()
                cur.execute(
                    query, (request.form['nameroom'], request.form['description'],))
                mysql.connection.commit()

                cur.close()

        rep = make_response(redirect("/kieuphong"))
    else:
        return rep

    return rep


@app.route("/suakieuphong", methods=['POST'])  # /addkieuphong
def get_page_suakieuphong():
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}

        if request.method == 'POST':
            if(("idroom" in request.form) and ('suanameroom' in request.form) and ('suanumbera' in request.form) and ('suanumberc' in request.form) and ('suadescription' in request.form)):
                query = "UPDATE room_type SET name=%s , description=%s , number_adult=" + \
                    str(request.form["suanumbera"])+" , number_children="+str(
                        request.form["suanumberc"])+" WHERE id="+str(request.form["idroom"])

                cur = mysql.connection.cursor()
                cur.execute(
                    query, (request.form['suanameroom'], request.form['suadescription'],))
                mysql.connection.commit()

                cur.close()

        rep = make_response(redirect("/kieuphong"))
    else:
        return rep

    return rep


@app.route("/xoakieuphong", methods=['POST'])  # /addkieuphong
def get_page_xoakieuphong():
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}

        if request.method == 'POST':
            if(('idroom' in request.form)):
                query = "UPDATE room_type SET status_check=0 WHERE id=" + \
                    str(request.form["idroom"])
                cur = mysql.connection.cursor()
                cur.execute(query, )
                mysql.connection.commit()

                cur.close()

                #rep = make_response(redirect(route_admin))

        rep = make_response(redirect("/kieuphong"))
    else:
        return rep

    return rep

# todo : giá


@app.route("/getpricebyid", methods=['POST'])  # /gia tien kieu phong
def get_pricebyid():
    # print(request.cookies.get('token'))
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}
        if request.method == 'POST':
            a = json.loads(request.data)

            #print(a)
            cur = mysql.connection.cursor()
            cur.execute(
                "SELECT * FROM room_type WHERE status_check = 1 AND id = "+str(a))

            data2 = cur.fetchall()
            #data2 = np.asarray(data2)

            print(data2)

            cur.close()
            return jsonify(data2)

    return {}

@app.route("/capnhatgia", methods=['POST'])  # /addkieuphong
def get_page_capnhatgia():
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}

        if request.method == 'POST':
            if(("idroom" in request.form)):

                idgiagio = 'NULL'
                idgiangay = 'NULL'
                idroom = str(request.form['idroom'])

                if('idgiagio' in request.form and request.form['idgiagio'] != "" ):
                    #print(request.form['idgiagio'])
                    idgiagio = str(request.form['idgiagio'])
                else:
                    print("null idgiagio")

                if('idgiangay' in request.form and request.form['idgiangay'] != ""):
                    #print(request.form['idgiangay'])
                    idgiangay = str(request.form['idgiangay'])
                else:
                    print("null idgiangay")
                
                
                if('giagio' in request.form):

                    print(request.form['giagio'])
                    #request.args.get("status")
                    #print(request.form.getlist("sogiotheogio[]"))    
                    #print(request.form.getlist("sotientheogio[]"))
                    if('sogiotheogio[]' in request.form and 'sotientheogio[]' in request.form):
                        
                        print(request.form.getlist("sogiotheogio[]"))    
                        print(request.form.getlist("sotientheogio[]"))

                        query = "INSERT INTO price (number,price,order,number_children) VALUES (%s, %s, "+str(
                        request.form["numbera"])+","+str(request.form["numberc"])+")"
                        cur = mysql.connection.cursor()
                        cur.execute(
                            query, (request.form['nameroom'], request.form['description'],))
                        mysql.connection.commit()

                        cur.close()

                        data2 = cur.fetchall()

                    else:
                        idgiagio = 'NULL'
                else:
                    pass

                    
                if('giangay' in request.form):
                    print(request.form['giangay'])
                
                

        rep = make_response(redirect("/kieuphong"))
    else:
        return rep

    return rep
# * Tầng


@app.route("/tang")  # /tang
def get_page_tang():
    # print(request.cookies.get('token'))
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM room_level WHERE status_check = 1 ORDER BY name ASC")

        data2 = cur.fetchall()
        data2 = np.asarray(data2)

        # print(data2)

        cur.close()
    else:
        return rep

    return render_template("admin/tang.html", data=data, data2=data2)


@app.route("/addtang", methods=['POST'])  # /addkieuphong
def get_page_addtang():
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}

        if request.method == 'POST':
            if(('nametang' in request.form) and ('description' in request.form)):
                query = "INSERT INTO room_level (name,description) VALUES (%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(
                    query, (request.form['nametang'], request.form['description'],))
                mysql.connection.commit()

                cur.close()

        rep = make_response(redirect("/tang"))
    else:
        return rep

    return rep


@app.route("/suatang", methods=['POST'])  # /addkieuphong
def get_page_suatang():
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}

        if request.method == 'POST':
            if(("idroom" in request.form) and ('suanametang' in request.form) and ('suadescription' in request.form)):
                query = "UPDATE room_level SET name=%s , description=%s WHERE id=" + \
                    str(request.form["idroom"])

                cur = mysql.connection.cursor()
                cur.execute(
                    query, (request.form['suanametang'], request.form['suadescription'],))
                mysql.connection.commit()

                cur.close()

        rep = make_response(redirect("/tang"))
    else:
        return rep

    return rep


@app.route("/xoatang", methods=['POST'])  # /addkieuphong
def get_page_xoatang():
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}

        if request.method == 'POST':
            if(('idtang' in request.form)):
                query = "UPDATE room_level SET status_check=0 WHERE id=" + \
                    str(request.form["idtang"])
                cur = mysql.connection.cursor()
                cur.execute(query, )
                mysql.connection.commit()

                cur.close()

                #rep = make_response(redirect(route_admin))

        rep = make_response(redirect("/tang"))
    else:
        return rep

    return rep


# * phòng


@app.route("/phong")  # /phong
def get_page_phong():
    # print(request.cookies.get('token'))
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM room WHERE status_check = 1 ORDER BY name ASC")
        data2 = cur.fetchall()
        data2 = np.asarray(data2)
        cur.close()

        # find all room_type avalible
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM room_type WHERE status_check = 1")
        room_type = cur.fetchall()
        room_type = np.asarray(room_type)
        cur.close()
        # print(room_type)
        # find all room_level avalible
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM room_level WHERE status_check = 1 ORDER BY name ASC")
        room_level = cur.fetchall()
        room_level = np.asarray(room_level)
        cur.close()
        # print(room_level)

    else:
        return rep

    return render_template("admin/phong.html", data=data, data2=data2, room_type=room_type, room_level=room_level)


@app.route("/addphong", methods=['POST'])  # /addkieuphong
def get_page_addphong():
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}

        if request.method == 'POST':
            if(('namephong' in request.form) and ('description' in request.form) and ('selectkieuphong' in request.form) and ('selecttang' in request.form)):
                query = "INSERT INTO room (name,description,room_type,room_level) VALUES (%s, %s,"+str(
                    request.form['selectkieuphong'])+","+str(request.form['selecttang'])+")"
                cur = mysql.connection.cursor()
                cur.execute(
                    query, (request.form['namephong'], request.form['description'],))
                mysql.connection.commit()

                cur.close()

        rep = make_response(redirect("/phong"))
    else:
        return rep

    return rep


@app.route("/suaphong", methods=['POST'])  # /addkieuphong
def get_page_suaphong():
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}

        if request.method == 'POST':
            if(("idroom" in request.form) and ('suanamephong' in request.form) and ('suadescription' in request.form) and ('suaselectkieuphong' in request.form) and ('suaselecttang' in request.form)):
                query = "UPDATE room SET name=%s , description=%s,room_type=" + \
                    str(request.form["suaselectkieuphong"])+",room_level="+str(
                        request.form["suaselecttang"])+" WHERE id="+str(request.form["idroom"])

                cur = mysql.connection.cursor()
                cur.execute(
                    query, (request.form['suanamephong'], request.form['suadescription'],))
                mysql.connection.commit()

                cur.close()

        rep = make_response(redirect("/phong"))
    else:
        return rep

    return rep


@app.route("/xoaphong", methods=['POST'])  # /addkieuphong
def get_page_xoaphong():
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session and level == level_admin):
        data = {"username": session.get('username'),
                "level": session.get('level')}

        if request.method == 'POST':
            if(('idphong' in request.form)):
                query = "UPDATE room SET status_check=0 WHERE id=" + \
                    str(request.form["idphong"])
                cur = mysql.connection.cursor()
                cur.execute(query, )
                mysql.connection.commit()

                cur.close()

                #rep = make_response(redirect(route_admin))

        rep = make_response(redirect("/phong"))
    else:
        return rep

    return rep


# Receptionist
# * so do phong


@app.route("/sodophong")  # /sodophong
def get_page_sodophong():
    # print(request.cookies.get('token'))
    isTrue, rep, id_user, username_user, token_user, level = token.checktoken(
        request.cookies, mysql)

    if(isTrue and "username" in session):
        #print(username_user+" "+token_user+" "+str(level))

        data = {"username": session.get('username'),
                "level": session.get('level')}

    else:
        return rep

    return render_template("admin/sodophong.html", data=data)


if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)
