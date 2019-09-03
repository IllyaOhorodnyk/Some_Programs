import json
import os
import sys


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
