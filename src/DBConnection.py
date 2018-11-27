import psycopg2
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import *
from decimal import Decimal


conn = psycopg2.connect(host="reddwarf.cs.rit.edu", port="5432", user="p32004z", password="ahD4cheo9uw9ie2Ighai")
cur = conn.cursor()

app = Flask(__name__)
CORS(app, supports_credential=True)


@app.route('/AllTrucks', methods=['GET'])
def get_all_trucks():
    mylist = []
    cur.execute("select * from customerbankcard")
    for data in cur:
        print(data)
        mylist.append(data)
    return jsonify(mylist)


@app.route('/AllPackages', methods=['GET'])
def get_all_packages():
    mylist = []
    cur.execute("select * from package")
    for data in cur:
        print(data)
        mylist.append(data)
    return jsonify(mylist)


@app.route('/AllCards', methods=['GET'])
def get_all_cards():
    mylist = []
    cur.execute("select * from trail")
    for data in cur:
        print(data)
        mylist.append(data)
    print(mylist)
    return jsonify(mylist)


@app.route('/UserAllPackages', methods=['GET'])
def get_user_all_packages():
    mylist = []
    userId = request.args.get("userId")
    cur.execute("select * from package where customer_id = " + "'" + userId + "'")
    for data in cur:
        mylist.append(data)
    print(mylist)
    return jsonify(mylist)


@app.route('/AllUsers', methods=['GET'])
def get_all_users():
    mylist = []
    cur.execute("select * from customer order by char_length(customer_id), customer_id asc")
    for data in cur:
        print(data)
    return jsonify(mylist)


@app.route('/UserOnePackage', methods=['GET'])
def get_one_user_package():
    mylist = []
    packageID = request.args.get("packageId")
    cur.execute("select * from package where package_id = " + "'" + packageID + "'")
    for data in cur:
        for detail in data:
            mylist.append(detail)

    cur.execute("select * from address where address_id = " + "'" + mylist[3] + "'")
    for data in cur:
        print(data)
        mylist.append(data)

    return jsonify(mylist)


@app.route('/CreateUser', methods=['GET'])
def create_user():
    mylist = []
    countlist = []
    name = "'" + request.args.get("name") + "'"
    email = "'" + request.args.get("email") + "'"
    phonen = "'" + request.args.get("phnum") + "'"
    password = "'" + request.args.get("password") + "'"
    count = 0
    cur.execute("select * from customer order by char_length(customer_id),customer_id asc")
    for data in cur:
        count += 1
        countlist.append(data[0])

    id = int(countlist[count - 1]) + 1
    cid = "'" + str(id) + "'"
    cur.execute("insert into customer(customer_id, name,email,phone_number,password) values " + "(" + cid + "," + name + "," + email + "," + phonen + "," + password + ")")
    conn.commit()
    cur.execute("select * from customer")
    for data in cur:
        print(data)
        mylist.append(data)
    return jsonify(cid)


@app.route('/AddBankAccount', methods=['POST'])
def create_bank_account():
    mylist = []
    uid = "'" + request.args.get("uid") + "'"
    accountn = "'" + request.args.get("accountn") + "'"
    routingn = "'" + request.args.get("routingn") + "'"

    cur.execute("insert into bankaccount values " + "(" + uid + "," + accountn + "," + routingn + ")")
    conn.commit()

    cur.execute("select * from bankaccount where customer_id = " + uid)
    for data in cur:
        print(data)
        mylist.append(data)
    return jsonify(mylist)


@app.route('/AddBankCard', methods=['POST'])
def create_bank_card():
    mylist = []
    uid = "'" + request.args.get("uid") + "'"
    cname = "'" + request.args.get("holder_name") + "'"
    cardn = "'" + request.args.get("card_number") + "'"
    cvv2 = "'" + request.args.get("cvv2") + "'"
    month = "'" + request.args.get("month") + "'"
    year = "'" + request.args.get("year") + "'"

    countlist = []
    count = 0
    cur.execute("select * from customerbankcard order by char_length(card_id),card_id asc")
    for data in cur:
        count += 1
        countlist.append(data[0])

    id = int(countlist[count - 1]) + 1
    cid = "'" + str(id) + "'"


    cur.execute("insert into customerbankcard values (" + cid + "," + uid + "," + cname + "," + cardn + "," + cvv2 + "," + year + "," + month + ")")
    conn.commit()

    cur.execute("select * from customerbankcard where customer_id = " + uid)
    for data in cur:
        print(data)
        for detail in data:
            if isinstance(detail, Decimal):
                mylist.append(str(detail))
            else:
                mylist.append(detail)
    return jsonify(mylist)


@app.route('/AddAddress', methods=['POST'])
def add_address():
    mylist = []
    aptn = "'" + request.args.get("aptn") + "'"
    strn = "'" + request.args.get("strname") + "'"
    st = "'" + request.args.get("strn") + "'"
    city = "'" + request.args.get("city") + "'"
    state = "'" + request.args.get("state") + "'"
    country = "'" + request.args.get("country") + "'"
    zip = "'" + request.args.get("zip") + "'"
    countlist = []
    count = 0
    cur.execute("select * from address order by char_length(address_id),address_id asc")
    for data in cur:
        count += 1
        countlist.append(data[0])

    id = int(countlist[count - 2]) + 1
    cid = "'" + str(id) + "'"

    cur.execute("insert into address values (" + cid + "," + aptn + "," + st + "," + strn + "," + city + "," + state + "," + zip + "," + country + ")")
    conn.commit()

    return jsonify(mylist)


@app.route('/AddOneUserPackage', methods=['POST'])
def add_one_user_package():
    mylist = []

    uid = "'" + request.args.get("uid") + "'"
    vid = "'" + request.args.get("vid") + "'"
    aid = "'" + request.args.get("aid") + "'"
    did = "'" + request.args.get("did") + "'"
    speed = "'" + request.args.get("speed") + "'"
    type = "'" + request.args.get("type") + "'"
    weight = "'" + request.args.get("weight") + "'"
    haz = "'" + request.args.get("haz") + "'"

    countlist = []
    count = 0
    cur.execute("select * from package order by char_length(package_id),package_id asc")
    for data in cur:
        count += 1
        countlist.append(data[0])

    id = int(countlist[count - 1]) + 1
    cid = "'" + str(id) + "'"

    cur.execute("insert into package values(" + cid + "," + uid + "," + vid + "," + '505' + "," + did + "," + speed + "," + type + "," + weight + "," + haz + ")")
    conn.commit()

    return jsonify(mylist)


# @app.route('/DeleteOneUserPackage', methods=['DELETE'])
# def delete_one_user_packages(trackingId):
#     mylist = []
#     cur.execute("select * from  where ")
#     return mylist


@app.route('/UserLogin', methods=['GET'])
def user_login():
    mylist = []
    e = request.args.get("email")
    p = request.args.get("password")
    cur.execute("select * from customer where email = " + "'" + e + "'" + " and password = " + "'" + p + "'")
    for data in cur:
        print(data)
        for detail in data:
            mylist.append(detail)
    return jsonify(mylist)


@app.route('/UserInfo', methods=['GET'])
def get_user_info():
    mylist = []
    userId = "'" + request.args.get("userId") + "'"
    cur.execute("select * from customer,bankaccount where customer.customer_id = " + userId + " and bankaccount.customer_id = " + userId)
    for data in cur:
        print(data)
        for detail in data:
            mylist.append(detail)
    cur.execute("select * from customerbankcard where customer_id = " + userId)
    for data in cur:
        for detail in data:
            mylist.append(str(detail))
    return jsonify(mylist)


@app.route('/package_Address', methods=['GET'])
def get_user_address_info():
    mylist = []
    cur.execute("select * from address")
    for data in cur:
        print(data)
    return jsonify(mylist)


@app.route('/AllAddress', methods=['GET'])
def get_address_info():
    mylist = []
    cur.execute("select * from address")
    for data in cur:
        print(data)
    return jsonify(mylist)


app.run(debug=True)
cur.close()
conn.close()
