# app.py
from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import json
import shutil # Import shutil for file cloning

app = Flask(__name__)

# Configuration
JSONL_DIR = 'jsonl_files'
os.makedirs(JSONL_DIR, exist_ok=True)

def list_jsonl_files():
    files = [f for f in os.listdir(JSONL_DIR) if f.endswith('.jsonl')]
    return files

def read_jsonl_file(filename):
    filepath = os.path.join(JSONL_DIR, filename)
    if not os.path.exists(filepath):
        return None
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                return "JSON decode error in file"
    return data

def write_jsonl_file(filename, data):
    filepath = os.path.join(JSONL_DIR, filename)
    try:
        with open(filepath, 'w') as f:
            for item in data:
                json.dump(item, f)
                f.write('\n')
        return True
    except Exception as e:
        return str(e)

def create_jsonl_file(filename):
    filepath = os.path.join(JSONL_DIR, filename)
    if os.path.exists(filepath):
        return "File already exists"
    try:
        with open(filepath, 'w') as f: # Create an empty file
            pass # No content needed for a new empty JSONL
        return True
    except Exception as e:
        return str(e)

def clone_jsonl_file(filename, new_filename):
    filepath = os.path.join(JSONL_DIR, filename)
    new_filepath = os.path.join(JSONL_DIR, new_filename)
    if not os.path.exists(filepath):
        return "Source file not found"
    if os.path.exists(new_filepath):
        return "Destination file already exists"
    try:
        shutil.copy2(filepath, new_filepath) # copy2 to preserve metadata
        return True
    except Exception as e:
        return str(e)


@app.route('/')
def index():
    # Render a basic index.html, file list will be loaded by JS
    return render_template('index.html')

@app.route('/api/listFiles')
def listFiles():
    files = list_jsonl_files()
    return jsonify(files=files)

@app.route('/api/loadFile')
def loadFile():
    filename = request.args.get('file')
    if not filename:
        return jsonify(error="File parameter is missing"), 400
    data = read_jsonl_file(filename)
    if data is None:
        return jsonify(error="File not found"), 404
    if isinstance(data, str): # Error message from read_jsonl_file
        return jsonify(error=data), 400
    return jsonify(data=data)

@app.route('/api/save', methods=['POST'])
def saveFile():
    filename = request.args.get('file')
    if not filename:
        return jsonify(error="File parameter is missing"), 400
    data = request.get_json()
    if data is None:
        return jsonify(error="No JSON data provided"), 400

    # Validate data structure (optional, but good practice) - same validation as before
    if not isinstance(data, list):
        return jsonify(error="Data must be a list of JSON objects"), 400
    for item in data:
        if not isinstance(item, dict) or 'messages' not in item:
            return jsonify(error="Each item must be a dict with 'messages' key"), 400
        if not isinstance(item['messages'], list):
            return jsonify(error="'messages' must be a list"), 400
        for msg in item['messages']:
            if not isinstance(msg, dict) or 'role' not in msg or 'content' not in msg:
                return jsonify(error="Each message in 'messages' must have 'role' and 'content'"), 400

    result = write_jsonl_file(filename, data)
    if result is True:
        return jsonify(success=True)
    else:
        return jsonify(error="Failed to save file: " + str(result)), 500

@app.route('/api/createFile')
def createFile():
    filename = request.args.get('file')
    if not filename:
        return jsonify(error="File parameter is missing"), 400
    if not filename.endswith('.jsonl'):
        return jsonify(error="Filename must end with '.jsonl'"), 400

    result = create_jsonl_file(filename)
    if result is True:
        return jsonify(success=True, filename=filename) # Return filename for easy loading in frontend
    else:
        return jsonify(error="Failed to create file: " + str(result)), 500

@app.route('/api/cloneFile')
def cloneFile():
    filename = request.args.get('file')
    new_filename = request.args.get('new_file')
    if not filename or not new_filename:
        return jsonify(error="File and new_file parameters are required"), 400
    if not new_filename.endswith('.jsonl'):
        return jsonify(error="New filename must end with '.jsonl'"), 400

    result = clone_jsonl_file(filename, new_filename)
    if result is True:
        return jsonify(success=True, filename=new_filename) # Return new filename
    else:
        return jsonify(error="Failed to clone file: " + str(result)), 500


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
