import requests
import subprocess
import schedule
from time import sleep
import base64


def getConfigs():
    servers = requests.get('https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/subscribe/protocols/reality')
    if servers.status_code != 200:return False
    try:
        servers = base64.b64decode(servers.text).decode('utf-8')
    except:
        servers = servers.text
    with open('config.txt', 'w', encoding='UTF-8') as file: file.write(servers)
    return True
    


def runTest():
    subprocess.call(['./xray-knife', 'net', 'http', '-f', 'config.txt', '-u', 'https://youtube.com', '-s'])


def main():
    if not getConfigs(): return
    runTest()

schedule.every(15).minutes.do(main)

if __name__ == "__main__":
    print("#=> Started")
    main()
    while True:
        schedule.run_pending()
        sleep(1)

