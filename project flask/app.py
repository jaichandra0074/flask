from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
class ICICI_ATM:

    def __init__(self, name, dob, pin, balance):

        self.name = name
        self.dob = dob
        self.pin = pin
        self.balance = balance


    def check_pin(self, entered_pin):

        return entered_pin == self.pin


    def check_balance(self):

        return self.balance


    def withdraw(self, amount):

        if amount <= 0:

            return "Enter valid amount"


        elif amount > self.balance:

            return "Insufficient Balance"


        elif amount % 100 != 0:

            return "Amount should be multiples of 100"


        else:

            self.balance -= amount

            return f"""
            ₹{amount} Withdraw Successful <br>
            Remaining Balance : ₹{self.balance}
            """


    def deposit(self, amount):

        if amount < 100:

            return "Minimum deposit is ₹100"


        elif amount % 100 != 0:

            return "Deposit amount should be multiples of 100"


        else:

            self.balance += amount

            return f"""
            ₹{amount} Deposited Successfully <br>
            Updated Balance : ₹{self.balance}
            """



    def change_pin(self, old_pin, new_pin, confirm_pin):

        if old_pin != self.pin:

            return "Wrong Old PIN"


        elif len(new_pin) != 6:

            return "PIN should be 6 digits"


        elif new_pin != confirm_pin:

            return "PIN mismatch"


        else:

            self.pin = new_pin

            return "PIN Changed Successfully"



    def account_details(self):

        return {

            "name": self.name,

            "dob": self.dob,

            "balance": self.balance
        }




user1 = ICICI_ATM(

    "Neduri Jaichandra Dasaradha Ramayya",

    "15-06-2004",

    "113374",

    200000
)



@app.route("/")

def home():

    return render_template("index.html")




@app.route("/login", methods=["POST"])

def login():

    data = request.get_json()

    entered_pin = data["pin"]

    if user1.check_pin(entered_pin):

        return jsonify({

            "status": "success",

            "message": "Login Successful"
        })

    else:

        return jsonify({

            "status": "error",

            "message": "Incorrect PIN"
        })



@app.route("/balance")

def balance():

    return jsonify({

        "balance": user1.check_balance()
    })




@app.route("/withdraw", methods=["POST"])

def withdraw():

    data = request.get_json()

    amount = int(data["amount"])

    result = user1.withdraw(amount)

    return jsonify({

        "message": result
    })


@app.route("/deposit", methods=["POST"])

def deposit():

    data = request.get_json()

    amount = int(data["amount"])

    result = user1.deposit(amount)

    return jsonify({

        "message": result
    })



@app.route("/change_pin", methods=["POST"])

def change_pin():

    data = request.get_json()

    old_pin = data["old_pin"]

    new_pin = data["new_pin"]

    confirm_pin = data["confirm_pin"]

    result = user1.change_pin(

        old_pin,

        new_pin,

        confirm_pin
    )

    return jsonify({

        "message": result
    })




@app.route("/details")

def details():

    return jsonify(

        user1.account_details()
    )



if __name__ == "__main__":

    app.run(debug=True)