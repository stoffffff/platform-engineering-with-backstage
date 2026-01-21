from flask import Flask, jsonify
import socket, datetime

app = Flask(__name__)

@app.route("/main")
def home():
    return jsonify({
        'message': "Welcome to the Home Page!", 
        'status': "success",
        'hostname': socket.gethostname(),
        'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y")
        })
@app.route("/hello")
def home():
    return "Hello There ! :)"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

