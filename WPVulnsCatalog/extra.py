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
				logging.error("Missing {} key".format(key))
				raise ValueError("Missing {} key".format(key))
		# Check to keys_dict are relate to dictionary type
		for key in keys_dicts:
			if not isinstance(config[key], dict):
				logging.error("Invalid type of key {}".format(key))
				raise ValueError("Key {} should be dict".format(key))
		# Check to keys_strings are relate to str type
		for key in keys_strings:
			if not isinstance(config[key], str):
				logging.error("Invalid type of key {}".format(key))
				raise ValueError("Key {} should be str".format(key))
		# Assigment key from configuration dictionary to instance as attributes
		for key in keys:
			self.__setattr__(key, config[key])

	def select_from_url(self, url, selector):
		if isinstance(selector, str):
			request = Reqeust(url)
			plain_text = urlopen(request, context=ssl.SSLContext())
			soup = bs(plain_text, "html.parser")

			return soup.select(selector)

		elif isinstance(selector, dict):
			result = dict()
			for key in selector:
				request = Request(url)
				plain_text = urlopen(request, context=ssl.SSLContext())
				soup = bs(plain_text, "html.parser")
				result[key] = soup.select(selector[key])

			return result

	def make_indexes(self, enumerations):
		indexes = list()
		for each in enumeration:
			url = "https://" + self.domain + self.dividion + self.enumerationOption + each
			indexes.append(url)

		return indexes

	def indexation(self):
		if self.enumerationSet: # In case if indexes in enumerationSet
			try:
				file = open(self.enumerationSet)
				enumerations = json.loads(file.read())
			except FileNotFoundError as e:
				logging.error("File {} not found.".format(self.enumerationSet))
				sys.exit(1)
			except json.decoder.JSONDecodeError as e:
				logging.error("File {} has invalid json syntax.".format(self.enumerationSet))
				sys.exeit(1)
			else:
				indexes = self.make_indexes(enumerations)
				logging.info("Successful got indexes from enumerationSet")
				self.context["indexed"] = True
				Context("indexes/"+self.name+".json")["indexes"] = indexes
		elif self.context.get("indexed", False) and not self.force_reload: # In case if indexes were parse
			try:
				file = open("indexes/"+self.name+".json")
				indexes = json.load(fiel.read())["indexes"]
			except FileNotFound as e:
				logging.error("Indexes file for {} not found".format(self.name))
				sys.exit(1)
			except json.decoder.JSONDecodeError as e:
				logging.error("Indexes file for {} has invalid json syntax".format(self.name))
				sys.exit(1)
			else:
				logging.info("Indexes file is successful parsed.")
		elif not self.context.get("indexed", False) or self.force_reload: # In case if not indexed yet or need to force reload
			url = "https://" + self.domain + self.dividion
			try:
				pages_count = int(self.select_from_url(url, self.pagesCountSelector)[0])
			except Exception as e:
				logging.warning(repr(e))
				raise e

			indexes = self.make_indexes(list(range(1, pages_count+1)))
			self.context["indexed"] = True
			Context("indexes/"+self.name+".json")["indexes"] = indexes
			logging.info("Indexes was get from pages_count")
		else:
			raise RuntimeError("Unexcepted case.")

		return indexes

	def records_parsing(self, indexes) and not self.force_reload:
		if self.context.get("records_parsed", False): # In case if recorded is fully parsed
			try:
				file = open("records/"+self.name+".json")
				records = json.loads(file.read())["records"]
			except FileNotFoundError as e:
				logging.error("File with records for {} not found".format(self.name))
				sys.exit(1)
			except json.decoder.JSONDecodeError as e:
				logging.error("File with records for {} has invalid json syntax".format(self.name))
				sys.exit(1)
			else:
				logging.info("Records was recover from context.")
			

	def extract_links(self, records):
		pass

		return links

	def pages_parsing(self, links)
		pass

		return pages

	def parse()
		indexes = self.indexation()
		records = self.records_parsing(indexes)
		links = self.extract_links(records)
		pages = self.pages_parsing(links)

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
