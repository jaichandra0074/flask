'''
WEB
---
----->(WWW) THE WORLD WIDE WEB IS A COLLECTION OF WEBSITES AND WEBPAGES CONNECTED THROUGH THE NETWORK WHERE USER CAN ACCESS THESE WEBSITES USING WEB
WEN BROWSERS.

WEB BROWSERS
------------
A WEB BROWSER IS A SOFTWARE USED TO ACCESS AND DISPALY WEBPAGES

WEB SERVER
----------
--->A WEB SERVER STORES WEBSITES FILES AND SENDS WEBPAGES TO USERS WHEN THEY REQUEST THROUGH A BROWSER...

WEB APPLICATION
---------------
--->A WEB APPLICATION IS A SOFTWARE THAT RUNS AND SENDS INSIDE A BROWSER AND ALLOWS USER 


from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "welcome to flask Application"
if __name__ == '__main__':
    app.run(debug=True)'''
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(to right, #1e3c72, #2a5298);
                font-family: Arial, sans-serif;
            }

            .container {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                text-align: center;
            }

            h1 {
                color: #1e3c72;
                margin-bottom: 10px;
            }

            p {
                color: #555;
                font-size: 18px;
            }

            button {
                margin-top: 20px;
                padding: 10px 20px;
                border: none;
                background-color: #1e3c72;
                color: white;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
            }

            button:hover {
                background-color: #16325c;
            }
        </style>
    </head>
    <body>

        <div class="container">
            <h1>Welcome to Flask Application</h1>
            <p>Your Flask app is running successfully 🚀</p>
            <button>Get Started</button>
        </div>

    </body>
    </html>
                
    

if __name__ == '__main__':
    app.run(debug=True)

routing, url_for(),redirects and url converters
"""

'''
url_for()
-------------
---> this flask function used to dynamically generate urls for routes in flask

---> syntax --> url_for('function name')
'''
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    return f"welcome {username}"

@app.route('/student/<name>')
def home():
    return redirect(url_for('profile', username = 'neduri'))

if __name__ == '__main__':
    app.run(debug=True)

'''
dynamic routing
url -------> https:// 127.0.0.1:5000
---->
'''