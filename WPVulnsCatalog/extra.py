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
		# List of all keys
		keys = ["name", "domain", "dividion", "enumerationOption",
			"enumerationSet", "pagesCountSelector", "recordParseSelectors",
			"recordLinkSelector", "itemParseSelectors", "parserBypass"]
		# List of keys that relate to dictrionaty type
		keys_dicts = ["recordParseSelectors", "itemParseSelectors"]
		# List of keys that relate to string type
		keys_strings = ["name", "domain", "dividion", "enumerationOption", 
				"enumerationSet", "pagesCountSelector", "recordLinkSelector",
				"parserBypass"]
		# Check to all keys exist
		for key in keys:
			if not config.get(key, False):
				raise ValueError("Missing {} key".format(key))
		# Check to keys_dict are relate to dictionary type
		for key in keys_dicts:
			if not isinstance(config[key], dict):
				raise ValueError("Key {} should be dict".format(key))
		# Check to keys_strings are relate to str type
		for key in keys_strings:
			if not isinstance(config[key], str):
				raise ValueError("Key {} should be str".format(key))
		# Assigment key from configuration dictionary to instance as attributes
		for key in keys:
			self.__setattr__(key, config[key])

	def select_from_url(self, url, selector):
			request = Reqeust(url)
			plain_text = urlopen(request, context=ssl.SSLContext())
			soup = bs(plain_text, "html.parser")

			return soup.select(selector)

	def parse(self):
		### INDEXATION ###
		
		##################		
		
		### RECORDS_PARSING ###

		#######################
		
		### PAGE_PARSING ###

		####################

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
