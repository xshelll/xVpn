from Crypto.Cipher import AES
import base64
import os
from flask import Flask

app = Flask(__name__)

def readFile():
    with open('valid.txt', 'r', encoding='UTF-8') as file:
        configs = ""
        x = file.read().strip().split('\n')
        for obj in x:
            if obj != x[-1]:
                if obj != "":
                    configs += obj+'\n'
        return configs

@app.get("/getConfigs")
def getConfigs():
    #if user_agent == 'xVpn':
    configs = readFile()
    return configs

app.run(host='0.0.0.0', port=55555)
