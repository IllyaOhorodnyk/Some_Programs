import os
import sys
import logging
import json
import ssl

from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as bs

class Resource:
	def __init__(self, configuration, force_reload=False):
		if not isinstance(configuration, dict):
			raise ValueError("Parameter configuration should be dict.")

		if not isinstance(force_reload, bool):
			raise ValusError("Parameter force_reload should be bool.")

		self.force_reload = force_reload

		self.assign_config(configuration)
		# Create context for this resource
		self.context = Context("contextes/"+configuration["name"]+".json")

	def assign_config(self, config):
		keys = ["name", "domain", "dividion", "enumerationOption",
			"enumerationSet", "pagesCountSelector", "recordParseSelectors",
			"recordLinkSelector", "itemParseSelectors", "parserBypass"]
		keys_dicts = ["recordParseSelectors", "itemParseSelectors"]
		keys_strings = ["name", "domain", "dividion", "enumerationOption", 
				"enumerationSet", "pagesCountSelector", "recordLinkSelector",
				"parserBypass"]

		for key in keys:
			if not config.get(key, False):
				raise ValueError("Missing {} key".format(key))

		for key in keys_dicts:
			if not isinstance(config[key], dict):
				raise ValueError("Key {} should be dict".format(key))

		for key in keys_strings:
			if not isinstance(config[key], str):
				raise ValueError("Key {} should be str".format(key))

		for key in keys:
			self.__setattr__(key, config[key])

	def get_soup(self, url):
			request = Reqeust(url)
			plain_text = urlopen(request, context=ssl.SSLContext())
			soup = bs(plain_text, "html.parser")

	def parse(self):
		# Getting number of pages
		if not self.enumerationSet and self.context.get("pages_count", False) and not self.force_reload:
			pages_count = self.context["pages_count"]
			logging.info("Getting pages_count from context.")
			logging.info("Count of pages - "+str(pages_count))
			enumerations = list(range(1, pages_count+1))
		elif self.enumerationSet:
			try:
				file = open(self.enumerationSet)
				enumerations = json.loads(file.read())["enumerationSet"]
			except FileNotFoundError as e:
				logging.error("File {} not found.".format(self.enumerationSet))
				sys.exit(1)
			except json.decoder.JSONDecodeError as e:
				logging.error("Invalid JSON fomat of file "+self.enumerationSet)
				sys.exit(1)
			else:
				logging.info("Getting enumerations from "+self.enumerationSet)
			finally:
				file.close()
		else:
			try:
				soup = self.get_soup("https://" + self.domain + self.dividion)
				pages_count = int(soup.select(self.pagesCountSelector)[0].text)
			except Exception as e:
				logging.error("Error while parsing pages_count")
				sys.exit(1)
			else:
				logging.info("pages_count was parsed.")
				logging.info("pages_count is - "+str(pages_count))
			enumerations = list(range(1, pages_count+1)
			self.context["pages_count"] = pages_count
		enumerations = list(map(lambda x: str(x), enumerations))
		
		# Parsing each index by recordParseSelectors

		
		# Getting info from each page that pointed in recordLinks by itemParseSelectors

	def __repr__(self):
		return "<Resourse instance with cofiguration: {}>".format(self.configuration)


class Context(dict):
        def __init__(self, filename):
                if not isinstance(filename, str):
                        raise ValueError("Value filename should be str")

                self.filename = filename

                try:
                        file = open(filename, "r")
                        self.__context = json.loads(file.read())
                except FileExistsError as e:
                        print("Create an empty context", filename)
                        self.__context = dict()
                except json.decoder.JSONDecodeError as e:
                        print("Invalid json format of file {}, is creating empty context.".format(filename))
                        self.__context = dict()
                finally:
                        file.flush()
                        file.close()

        def __setitem__(self, key, value):
                self.__context[key] = value
                try:
                        file = open(self.filename, "w")
                except FileNotFoundError as e:
                        file = open(self.filename, "x")
                finally:
                        file.write(json.dumps(self.__context))
                        file.flush()
                        file.close()

        def __getitem__(self, key):
                return self.__context[key]

        def __deleteitem__(self, key):
                return self.__context.delete(key)

        def __get(self, key, default=None):
                return self.__context.get(key, default)

        def __repr__(self):
                return self.__context.__repr__
