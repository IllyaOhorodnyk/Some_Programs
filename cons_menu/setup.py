import setuptools


with open("README.md", 'r') as file:
	long_description = file.read()

setuptools.setup(
	name="cons-menu",
	version="0.0.1",
	author="Illya Ohorodnyk",
	author_email="illyaohorodnyk@gmail.com",
	description="Utility for create and use console menu.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/IllyaOhorodnyk/Some_Programs/cons-menu",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programing Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operation System :: OS Independent"
	],
)
