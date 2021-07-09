import json
import requests
from requests.exceptions import RequestException
import re
import time
import lxml

def get_one_page(url):
	try:
		headers = {
			'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
		}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parse_one_page(html):
	pattern = re.compile('<td class="titleColumn">(.*?).'
		+'<a.*?>(.*?)</a>'+
		'.*?"secondaryInfo">((.*?))</span>.*?</td>', re.S)
	items = re.findall(pattern, html)
	for item in items:
		yield{
				'index':item[0].strip()[:-1],
				'name':item[1],
				'year':item[2][1:5]
		}

def write_to_file(content):
	with open('imdb.txt', 'a', encoding='utf-8') as f:
		f.write(json.dumps(content)+'\n')

def main():
	url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
	html = get_one_page(url)
	for item in parse_one_page(html):
		print(item)
		write_to_file(item)

if __name__ == '__main__':
	main()