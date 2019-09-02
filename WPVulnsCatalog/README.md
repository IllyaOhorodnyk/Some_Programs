WordPress Vulnerability Catalog

Yet it is mirroring from wpvulndb.com

Config file structure:
	resources:
		domain;
		reign;
		increaseOption;
		pagesCountSelector; # Selector in CSS format
		rowsExtractorSelectors; # Internal dictionary of name elements that need extract and they value
		parserProtectionBypass; # Can be name of func


Procedure of parsing:
	- Getting number of pages
	- Indexing of all pages by rowsExtractorSelectors
	- Getting info from rows pages by $(nameNewSelector)s
