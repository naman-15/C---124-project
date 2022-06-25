
from flask import Flask, jsonify,request

app = Flask(__name__)

contact = [
    {
        "ID":1,
        "Contact":"9835269876",
        "Name":"Person 1",
        "Done" : False
    },
    {
        "ID":1,
        "Contact":"6538452813",
        "Name":"Person 2",
        "Done" : False
    }
]

@app.route('/')

def api():
    return "Api working"

@app.route('/get-data')

def getData():
    return jsonify({
        "data" : contact
    })

@app.route('/post-data', methods = ["POST"])

def postData():
    newContact = {
        "ID":contact[-1]['ID']+1,
        "Name":request.json["Title"],
        "Contact":request.json.get("Description",""),
        "Done" : False
    }
    contact.append(newContact)
    return jsonify({
        "status": "Success"
    })

if (__name__ ==  '__main__'):
    app.run()