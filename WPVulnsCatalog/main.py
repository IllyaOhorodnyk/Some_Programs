import os
import sys
import cons_menu
import json
import ssl
import logging
from urllib.request import Request, urlopen

from parser import Parser


def main():
	config = json.load(open("config.json"))
	
	url = "https://" + config["resources"][0]["domain"] + "/" + config["resources"][0]["reign"]
	headers = {"X-Mashape-Key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}
	gcontext = ssl.SSLContext()


	request = Request(url, headers=headers)
	data = urlopen(request, context=gcontext).read().decode("utf-8")

	parser = Parser()
	parser.feed(data)

if __name__ == "__main__":
	main()
