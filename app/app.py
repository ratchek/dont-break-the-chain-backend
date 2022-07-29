from User import User
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

temp_data = {"2021": {"1": ["1","3","5"], "3":["1","4","14"]}}
def print_data():
    return jsonify(temp_data)
def set_data(data):
    global temp_data
    temp_data = data

@app.route('/')
def index():
    return 'This is my api. There are many like it, but this one is mine.'

@app.route('/user/create', methods = ['POST'])
def create_user():
    email = request.json['email']
    password = request.json['password']
    user = User()
    if user.new_user(email, password):
        return "Success! Created user {}".format(user.id)
    else:
        return "User email already exists"  


@app.route('/cal')
def cal():
    user_id = request.json["user"]
    user = User()
    user.connect_to_user(user_id)
    cal = user.get_cal()
    return (jsonify(cal))

@app.route('/cal/flip_date', methods = ['POST'])
def flip_date():
    day = request.json["date"]['day'] 
    month = request.json["date"]['month'] 
    year = request.json["date"]['year'] 
    user_id = request.json["user"]
    user = User()
    user.connect_to_user(user_id)
    cal = user.get_cal()
    if year in cal:
        if month in cal[year]:
            if day in cal[year][month]:
                cal[year][month].remove(day)
            else:
                cal[year][month].append(day)      
        else: 
            cal[year][month] = [day]
    else:
        cal[year] = {month: [day]}
    user.save_cal(cal)  
    return "Success!"

# Overwrites the whole calendar with whatever the React page is sending over
@app.route('/cal/save', methods = ['POST'])
def save():
    cal = request.json["cal"]
    user_id = request.json["user"]
    user = User()
    user.connect_to_user(user_id)
    user.save_cal(cal)  
    return "Saved!" 
        

if __name__ == "__main__":
    app.run(debug=True)
