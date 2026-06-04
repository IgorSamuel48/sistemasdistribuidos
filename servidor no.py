from flask import Flask
import socket
import platform
import datetime
import psutil

app = Flask(__name__)

@app.route("/info")
def info():

    return {

        "hostname": socket.gethostname(),

        "sistema": platform.system(),

        "cpu": psutil.cpu_percent(),

        "memoria": psutil.virtual_memory().percent,

        "hora": str(datetime.datetime.now())
    }

app.run(host="0.0.0.0", port=5000)
