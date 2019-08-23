import sys


class Menu:
	def __init__(self, items, annotations=None):
		try:
			items.__iter__
		except AttributeError:
			raise ValueError("Items value should be Iterable!")

		try:
			if annotations:
				annotations.__iter__
		except AttributeError:
			raise ValueError("Annotations value should be Iterable!")
		
		if not all(map(lambda x: callable(x), items)):
			raise ValueError("Each element of items should be callable!")

		if annotations and not all(map(lambda x: isinstance(x, str), annotations)):
			raise ValueError("Each element of annotations should be str!")

		self.annotations = annotations
		if len(annotations) < len(items):
			self.annotations.extend([""] * (len(items) - len(annotations)))

		self.items = dict()
		for i in range(len(items)):
			self.items[str(i+1)] = items[i]

		self.items["0"] = sys.exit

		self.prompt = "Welcome to main menu. Please make the choose.\n"

		for i in range(len(self.annotations)):
			self.prompt += str(i+1) + ") {}\n"

		self.prompt = self.prompt.format(*self.annotations)
		self.prompt += "0) Exit from program.\n>>> "

	def run(self):
		while True:
			RES = input(self.prompt)
			self.items.get(RES, lambda: print("Not exists item!"))()



if __name__ == "__main__":
	main()
