import requests
import subprocess
import schedule
from time import sleep


def getConfigs():
    servers = requests.get('https://raw.githubusercontent.com/yebekhe/ConfigCollector/main/sub/vless')
    if servers.status_code != 200:return False
    servers = servers.text
    with open('config.txt', 'w', encoding='UTF-8') as file: file.write(servers)
    return True
    


def runTest():
    subprocess.call(['./xray-knife', 'net', 'http', '-f', 'config.txt'])


def main():
    if not getConfigs(): return
    runTest()

schedule.every(15).minutes.do(main)

if __name__ == "__main__":
    print("#=> Started")
    print("test")
    main()
    while True:
        schedule.run_pending()
        sleep(1)

