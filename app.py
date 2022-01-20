from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to MIDL"

@app.route("/passToMidl", methods=['GET'])
def get():
    return jsonify('')

if __name__ == "__main__":
    app.run(debug=True)
    