import requests
import sys
import time

if (len(sys.argv) >= 2):
    url = sys.argv[1]
else:
    url = 'https://www.antmoe.com/'
req = requests.get(url)
print(url, req, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
