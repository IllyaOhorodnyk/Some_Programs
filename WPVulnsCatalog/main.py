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

	# Create dictionary-like object to dynamic manage context
	context = Context("context.json")

	if context.get("pages_count") and not config["force_reload"]:
		pages_count = context["pages_count"]
	else:
		resources = config["resources"]
		url = "https://" + resources[0]["domain"] + "/" + resources[0]["dividion"]

		print("Getting cout of pages.")
		data = urlopen(url, context=ssl.SSLContext()).read().decode("utf-8").replace("\n", '')
		soup = bs(data, "html.parser")
		pages_count = soup.select(resources[1]["pagesCountSelector"])[0].get("href").split("=")[1]
		context["pages_count"] = pages_count

	print("Cout of pages is -", pages_count)

	if context.get("forse_reload") and os.path.exists("indexes.json"):
		print("Index of all pages.")
		indexes = dict()
	
		for i in range(1, int(pages_count)+1):
			print("Getting {i} page".format(i=i), end="\r")
			indexes["page_"+str(i)] = parse_main_page(url + "?" + resources[0]["increaseOption"] + "=" + str(i))

		try:
			file = open("indexes.json", "x")
		except FileExistsError:
			file = open("indexes.json", "w")
		finally:
			file.write(json.dumps(indexes, sort_keys=True, indent=4))
			file.flush()
			file.close()

		print("\nSucessfuly writed into indexes.json")

if __name__ == "__main__":
	main()
