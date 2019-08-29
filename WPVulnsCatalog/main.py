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


def parse_main_page(url):	
	request = Request(url)
	data = urlopen(request, context=ssl.SSLContext()).read().decode("utf-8").replace("\n", '')

	table = re.search(r"<tbody>(.*)</tbody>", data).group(1).replace("</tr>", "</tr>\n")
	rows = re.findall(r"<tr>(.*)</tr>", table)
	info = list()
	
	for i in range(len(rows)):
		row = rows[i]
		info.append(dict())

		info[i]["pluginLink"] = "/plugins/" +\
			 re.search(r"<a href=\"/plugins/(.{2,70})\">.{2,70}</a>", row).group(1)

		info[i]["vulnerabilityLink"] = "/vulnerabilities/" +\
			re.search(r"<a href=\"/vulnerabilities/(.{1,70})\">.{2,70}</a>", row).group(1)
		
		info[i]["created-at"] = re.search(r"<td class=\"created-at\">(.{10})</td>", row).group(1)

	return info


def parse_plugin_page(url):
	request = Request(url)
	data = urlopen(request, context=ssl.SSLContext()).read().decode("utf-8")
	soup = bs(data, "html.parser")
	info = dict()

	info['fullName'] = soup.find("h1").text
	info["vulnerabilities"] = list()
	for row in soup.find_all("tr"):
		row_dict = dict()
		row_dict["publishData"] = row.find("td").text
		row_dict["fixed_in"] = row.find(class_="fixed_in").text
		row_dict["vulnerabilityLink"] = row.find("a").get("href")
		row_dict["vulnerabilityName"] = row.find("a").text
		info["vulnerabilities"].append(row_dict)

	return info


def main():
	config = json.load(open("config.json"))
	resources = config["resources"]
	url = "https://" + resources[0]["domain"] + "/" + resources[0]["reign"]

	print("Getting cout of pages.")
	data = urlopen(url, context=ssl.SSLContext()).read().decode("utf-8").replace("\n", '')
	pages_count = re.search(r"<a href=\"/plugins\?page=(\d*)\">Last &raquo;</a>", data).group(1)
	print("Cout of pages is -", pages_count)

	print(parse_plugin_page("https://wpvulndb.com/plugins/nextgen-gallery"))

#	print("Index of all pages.")
#	indexes = dict()
#	
#	for i in range(1, int(pages_count)+1):
#		print("Getting {i} page".format(i=i), end="\r")
#		indexes["page_"+str(i)] = parse_main_page(url + "?" + resources[0]["reign"] + "=" + str(i))
#
#	try:
#		file = open("indexes.json", "x")
#	except FileExistsError:
#		file = open("indexes.json", "w")
#	finally:
#		file.write(json.dumps(indexes))
#		file.flush()
#		file.close()
#
#	print("\nSucessfuly writed into indexes.json")

if __name__ == "__main__":
	main()
