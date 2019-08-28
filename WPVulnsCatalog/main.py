import os
import sys
import cons_menu
import json
import ssl
import logging
import re
import urllib
from urllib.request import Request, urlopen


def parse_page():
	config = json.load(open("config.json"))
	
	url = "https://" + config["resources"][0]["domain"] + "/" + config["resources"][0]["reign"]
	headers = {"X-Mashape-Key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}
	gcontext = ssl.SSLContext()


	request = Request(url, headers=headers)
	data = urlopen(request, context=gcontext).read().decode("utf-8").replace("\n", '')

	table = re.search(r"<tbody>(.*)</tbody>", data).group(1).replace("</tr>", "</tr>\n")
	rows = re.findall(r"<tr>(.*)</tr>", table)
	
	for row in rows:
		print(re.search(r"<a href=\"/plugins/(.{2,70})\">(.{2,70})</a>", row).group(1))
		print(re.search(r"<a href=\"/vulnerabilities/(.{1,70})\">(.{2,70})</a>", row).group(1))
		print(re.search(r"<td class=\"created-at\">(.{10})</td>", row).group(1))


def main():
	config = json.load(open("config.json"))
	resources = config["resources"]
	url = "https://" + resources[0]["domain"] + "/" + resources[0]["reign"]
	headers = {"X-Mashape-Key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}
	gcontext = ssl.SSLContext()

	print("Getting cout of pages.")
	data = urlopen(url, context=gcontext).read().decode("utf-8").replace("\n", '')
	pages_count = re.search(r"<a href=\"/plugins\?page=(\d*)\">Last &raquo;</a>", data).group(1)
	print("Cout of pages is -", pages_count)


if __name__ == "__main__":
	main()
