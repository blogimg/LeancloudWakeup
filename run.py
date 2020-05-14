import requests
import sys
import time

if (len(sys.argv) >= 2):
    urls = sys.argv[1].split(',')
else:
    urls = ['https://www.antmoe.com/']
for url in urls:
    req = requests.get(url)
    print(url, req, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
