from html.parser import HTMLParser


class Parser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.ready = False
		self.raws = list()

	def handle_starttag(self, tag, attrs):
		if tag == "tbody":
			self.ready = True

		if self.ready and tag="tr":
			self.current = list()

	def handle_data(self, data):
		if self.ready:
			print("Data is -", data)

	def handle_endtag(self, tag):
		if self.ready and tag == "tbody":
			self.ready = False


def main():
	print("Hello, World!")


if __name__ == "__main__":
	main()
