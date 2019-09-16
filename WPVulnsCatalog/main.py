import os
import sys
import cons_menu
import json
import ssl
import logging
import re
import urllib
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as bs

from context import Context
from extra import Resource

def main():
	# Trying to load configuration file
	try:
		file = open("config.json", "r")
		config = json.loads(file.read())
	except FileNotFoundError as e:
		print("Configuration file confing.json not found.")
		sys.exit(1)
	except json.decoder.JSONDecodeError as e:
		print("Configuration has invalid format.")
		sys.exit(1)
	else:
		file.flush()
		file.close()

	# Create resource instance
	resource = Resource(config["resources"][0])

if __name__ == "__main__":
	main()
