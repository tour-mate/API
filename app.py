from flask import Flask, request, jsonify
from recomendation import *

app = Flask(__name__)

#http://127.0.0.1:5000/recc?location=spain&type=leisure
# https://github.com/zinedkaloc/ai-travel-planner
@app.route("/recc")
def recc():
    location = request.args.get('location')
    type =request.args.get('type')
    return recommend_hotel(location,type).to_json()