from flask import Flask, request, Response
import uuid
import json #from jsonpickle
#import numpy as np
#from PIL import Image
import sqlite3
# connect database
db = sqlite3.connect('user.db')
cursor = db.cursor()
#cursor.execute('''INSERT INTO users(id, name, phone, email)
#                  ('34234234','nik', '4454464564', 'cool@gmail.com'))

#db.commit()
cursor.execute('''SELECT * FROM users''')
rows = cursor.fetchall()
for row in rows:
    print(row)

if db:
    print("success")

def checkUser(email, cursor):
    cursor.execute('''SELECT * FROM users''')
    rows = cursor.fetchall()
    if rows > 0:
        return True

def insert(name, email, phone, cursor):
    checked = checkUser(email, cursor)
    if checked:
        cursor.execute('''INSERT INTO users VALUES (:id, :name, :phone, :email)", {'id': uuid.uuid1(), 'name': name, 'phone': phone, 'email' : email}''')
        db.commit()
        if checkUser(email, cursor):
            return True
        else:
            return False

# Initialize the Flask application
app = Flask(__name__)
# route http posts to this method
@app.route('/register', methods=['POST', 'GET'])
def register():
    db = sqlite3.connect('user.db')
    cursor = db.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        file = request.files
        if not name and not email and not phone:
            if not file:
                name = 'error'
        else:
            if file:
                name = 'ok'
        insert = cursor.execute('''INSERT INTO users VALUES (:id, :name, :phone, :email)''', {'id': 23223, 'name': name, 'phone': phone, 'email' : email})
        db.commit()
        if insert:
            print('INSERTEED!!!!!!!!!!!!!!!!!!!!')
        print(request.files, request.form)
        res = Response(name, status=200, mimetype='text/plain')
        return res
@app.route('/')
def home():
    return 'HELLO'

# start flask app
app.run(host="127.0.0.1", port=5000, debug=True)
'''
r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")
    '''