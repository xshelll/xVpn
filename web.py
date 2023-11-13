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

def encrypt(text):
    BLOCK_SIZE = 16
    def pad(data):
        return data + (BLOCK_SIZE - len(data) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(data) % BLOCK_SIZE)
    
    def encrypt(message, key):
        iv = os.urandom(BLOCK_SIZE)
        aes = AES.new(key, AES.MODE_CBC, iv)
        padded_message = pad(message)
        encrypted_message = aes.encrypt(padded_message.encode('utf-8'))
        return base64.b64encode(iv + encrypted_message).decode('utf-8')

    message = text
    key = b'xshell@@38461568'

    encrypted_message = encrypt(message, key)
    return encrypted_message

@app.get("/getConfigs")
def getConfigs():
    #if user_agent == 'xVpn':
    configs = readFile()
    #encrypted = encrypt(configs)
    return configs

app.run(host='0.0.0.0', port=55555)
