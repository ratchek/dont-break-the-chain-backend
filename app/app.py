from flask import Flask, request, jsonify
import json
app = Flask(__name__)


# client = pymongo.MongoClient("mongodb+srv://flask-server:<password>@dont-break-the-chain-ap.syle4ff.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test

temp_data = {"2021": {"1": ["1","3","5"], "3":["1","4","14"]}}
def print_data():
    return jsonify(temp_data)
def set_data(data):
    global temp_data
    temp_data = data

@app.route('/')
def index():
    return 'This is my api. There are many like it, but this one is mine.'

@app.route('/cal', methods = ['POST', 'GET'])
def get_cal():
    if request.method == 'GET':
        return print_data()
    if request.method == 'POST':
        day = request.json['day'] 
        month = request.json['month'] 
        year = request.json['year'] 
        if year in temp_data:
            if month in temp_data[year]:
                if day in temp_data[year][month]:
                    temp_data[year][month].remove(day)
                else:
                    temp_data[year][month].append(day)      
            else: 
                temp_data[year][month] = [day]
        else:
            temp_data[year] = {month: [day]}
    return "Success!"

# Overwrites the whole calendar with whatever the React page is sending over
@app.route('/cal/save', methods = ['POST'])
def save():
    cal = request.json
    set_data(cal)
    print(cal)
    print(print_data())
    return "Saved?" 
        

if __name__ == "__main__":
    app.run(debug=True)
