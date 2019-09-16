import os
import sys
import logging
import json
import ssl

from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as bs

class Resource:
	def __init__(self, configurationi, force_reload=False):
		if not isinstance(configuration, dict):
			raise ValueError("Parameter configuration should be dict.")

		if not isinstance(force_reload, bool):
			raise ValusError("Parameter force_reload should be bool.")

		self.force_reload = force_reload
		### BLOCK OF CHECK CONFIGURATION ###
		####################################
		self.configuration = configuration
		# Create context for this resource
		self.context = Context("contextes/"+configuration["name"]+".json")
			
	def get_soup(self, url):
			request = Reqeust(url)
			plain_text = urlopen(request, context=ssl.SSLContext())
			soup = bs(plain_text, "html.parser")

	def parse(self):
		# Getting number of pages
		if not self.config["enumerationSet"] and self.context.get("pages_count", False) and not self.force_reload:
			pages_count = self.context["pages_count"]
			logging.info("Getting pages_count from context.")
			logging.info("Count of pages - "+str(pages_count))
			enumerationSet = list(range(1, pages_count+1))
		elif self.config["enumerationSet"]:
			try:
				file = open(self.config["enumerationSet"])
				enumerationSet = json.loads(file.read())["enumerationSet"]
			except FileNotFoundError as e:
				logging.error("File {} not found.".format(self.config["enumerationSet"]))
				sys.exit(1)
			except json.decoder.JSONDecodeError as e:
				logging.error("Invalid JSON fomat of file "+self.config["enumerationSet"])
				sys.exit(1)
			else:
				logging.info("Getting enumerationSeet from "+self.config["enumerationSet"])
			finally:
				file.close()
		else:
			selector = self.config["pagesCountSelector"]
			try:
				soup = self.get_soup("https://"+self.config["domain"]+self.config["dividion"])
				pages_count = int(soup.select(selector)[0].text)
			except Exception as e:
				logging.error("Error while parsing pages_count")
				sys.exit(1)
			else:
				logging.info("pages_count was parsed.")
				logging.info("pages_count is - "+str(pages_count))
			enumerationSet = list(range(1, pages_count+1)
			self.context["pages_count"] = pages_count
		enumerationSet = list(map(lambda x: str(x), enumerationSet))
		# Parsing each index by recordParseSelectors
		self.indexes = Context("indexes/"+self.config["name"]+".json")
		last_index = self.context.get("lastIndex")
			
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
