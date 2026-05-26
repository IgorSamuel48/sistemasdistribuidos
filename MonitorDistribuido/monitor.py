from flask import Flask
import socket
import platform
import datetime
import psutil

app=Flask(__name__)

@app.route('/status')

def status():

    return {

        "Servidor":socket.gethostname(),

        "Sistema":platform.system(),

        "DataHora":str(datetime.datetime.now()),

        "CPU":str(psutil.cpu_percent())+"%",

        "Memoria":str(psutil.virtual_memory().percent)+"%"
    }

app.run(host='0.0.0.0',port=5000)
