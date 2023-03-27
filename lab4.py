# from https://pythonbasics.org/flask-rest-api/  

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_record', methods=['GET'])
def query_records():
    studentID = request.args.get("studentID")
    print(studentID)
    with open('./tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['studentID'] == studentID:
                return jsonify(record)
        return jsonify({'error': 'data not found'}), 404

@app.route('/create_record', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    with open('./tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('./tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)
       

@app.route('/update', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('./tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
            record = r
        else:
            r = record
            new_records.append(r)
    with open('./tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route('/', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open('./tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('./tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)



@app.route('/elections', methods=['POST'])
def create_election_record():
    record = json.loads(request.data)
    with open('./tmp/edata.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('./tmp/edata.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

@app.route('/get_election_record', methods=['GET'])
def query_election_records():
    electionid = request.args.get("electionid")
    print(electionid)
    with open('./tmp/edata.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['electionid'] == electionid:
                return jsonify(record)
        return jsonify({'error': 'data not found'}), 404
    
@app.route('/del_election', methods=['DELETE'])
def del_election_record():
    record = json.loads(request.data)
    new_records = []
    with open('./tmp/edata.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['electionid'] == record['electionid']:
                continue
            new_records.append(r)
    with open('./tmp/edata.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


@app.route('/votes', methods=['POST'])
def create_voting_record():
    record = json.loads(request.data)
    with open('./tmp/vdata.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        for r in records:
            if r['voter_id'] == record['voter_id']:
                return jsonify({'error': 'Cannot vote twice'}), 404

        records.append(record)
    with open('./tmp/vdata.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)   
app.run(debug=True)