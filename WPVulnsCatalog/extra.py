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
