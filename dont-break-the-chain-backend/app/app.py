from flask import Flask
import json
app = Flask(__name__)

temp_data = {"2021": {"1": [1,3,5], "3":[1,4,14]}}
j = json.dumps(temp_data)

@app.route('/')
def index():
    return 'This is my api. There are many like it, but this one is mine.'

@app.route('/cal')
def get_cal():
    return j    


if __name__ == "__main__":
    app.run()
