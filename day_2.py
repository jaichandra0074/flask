'''from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/marks/<int:score>')
def marks(score):
    return f"Marks = {score}"

@app.route('/')
def home():
    return redirect(url_for('marks', score = 67))

if __name__ == '__main__':
    app.run(debug = True)

'''
'''
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/price/<float:Bill>')
def marks(score):
    return f"Price = {Bill}"

@app.route('/')
def home():
    return redirect(url_for('price', Bill = 667.56))

if __name__ == '__main__':
    app.run(debug = True)
'''
'''
3.uuid converters
---------------------

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/user/<uuid:user_id>')
def user(user_id):
    return f"User ID = {user_id}"

@app.route('/')
def home():
    return redirect(url_for('user',user_id ="113e-4565-e789-12d4-1133740000000000000000"))

if __name__ == '__main__':
    app.run(debug = True)
'''
'''
                                      HTTP Request Methods
                                    --------------------------

this http request methods are user for communication between a client (brower/app) and a server in web developmentand apis.
1. GET request
---------------
'''
