import requests
import os

if not os.path.exists('images'):
	os.makedirs('images')
urls = open('urls.txt')
count = 0

for url in urls.readlines():
	if not url == '\n':
		response = requests.get(url)
		open('images/' + str(count) + '.png','wb').write(response.content)
		print('saved ' + str(count) + 'images')
		count += 1
