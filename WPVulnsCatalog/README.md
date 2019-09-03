WordPress Vulnerability Catalog

Yet it is mirroring from wpvulndb.com

Config file structure:
	resources:
		domain;
		dividion;
		enumerationOption;
		enumerationSet # Can be an empty
		pagesCountSelector; # Selector in CSS format
		recordParseSelecors; # Internal dictionary of name elements that need extract and they value
		recordLinkSelector; # Record link should be write in another list/dictonary
		itemParseSelectors; # 
		parserProtectionBypass; # Can be name of func


Procedure of parsing:
	- Getting number of pages
	- Getting all indexes by enumerationOption with enumerationSet
	- Parsing each index by recordParseSelectors
	- Getting info from each page that pointed in recordLinks itemParseSelectors


Structure of vulnerabilities storage:
	- Indexes (from 1 to pages_count)
	- Records (rows in indexed table)
	- Items (key-value set on each enumerated row)
