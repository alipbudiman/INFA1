from flask import Flask
from flask import render_template, redirect, request
import socket

app = Flask(__name__)

# def GetIPAdress():
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.connect(("8.8.8.8", 80))
#     ip_address = str(s.getsockname()[0])
#     s.close()
#     return ip_address

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def program():
    bash_h = request.args.get('bash')
    if bash_h:
        if bash_h == "access":
            return redirect("/bash")
    else:
        return render_template("index.html")

@app.route("/bash")
def bash():
    return "this is bash route"


if __name__ == '__main__':
    app.run(debug=True,port=5008,host="0.0.0.0")