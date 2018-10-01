from flask import Flask, jsonify, request

app = Flask(__name__)

entries = []


@app.route('/api/v1/entries', methods=['GET'])
def get_all_entries():
    # global entries
    print(entries)
    if len(entries) > 0:
        return jsonify({'entries': entries}), 200
    return jsonify({'message': 'no entries found'}), 400


@app.route('/api/v1/entries/<int:entry_id>', methods=['GET'])
def get_one_entry(entry_id):
    for entry in entries:
        if entry['entry_id'] == entry_id:
            return jsonify(entry), 200
    return jsonify({'message': 'no entry with that id'}), 404


@app.route('/api/v1/entries', methods=['POST'])
def create_entry():
    request_data = request.get_json(force=True)
    new_entry = dict()
    if len(entries) == 0:
        new_entry["entry_id"] = 1
    else:
        new_entry["entry_id"] = entries[-1]['entry_id']+1
    new_entry["entry_date"] = request_data["entry_date"]
    new_entry["details"] = request_data["details"]
    if new_entry["details"] == "":
        return jsonify({"message": "please input details"})
    entries.append(new_entry)

    return jsonify({'entries': new_entry}), 201


@app.route('/api/v1/entries/<int:entry_id>', methods=['PUT'])
def modify_an_entry(entry_id):
    request_data = request.get_json()
    for entry in entries:
        if entry["entry_id"] == entry_id:
            entries[0]['details'] = request_data["details"]
            return jsonify(entry), 200
    return jsonify({'message': 'no entry with that id'}), 404


if __name__ == '__main__':
    app.run(debug=True)
