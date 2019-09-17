WordPress Vulnerability Catalog

Yet it is mirroring from wpvulndb.com

Config file structure:
 * resources:
 * * name;
 * * domain;
 * * dividion;
 * * enumerationOption;
 * * enumerationSet # Name of .json file that contain a set or if empty will using range from 1 to pagesCount
 * * pagesCountSelector; # Selector in CSS format
 * * recordParseSelecors; # Internal dictionary of name elements that need extract and CSS selector thar extracts it
 * * recordLinkSelector; # This selector can be in recordParseSelectors
 * * itemParseSelectors; # Internal dictionary of name elements that need extract and CSS selector that extracts it
 * * parserProtectionBypass; # Can be name of func


Procedure of parsing:
 * Create indexes (enumerable object that contain list of values for enumerationOption parameter)
    config["enumerationOption"], config["enumerationSet"], config["pagesCountSelector"] ==> {INDEXATION} ==> indexes(context protected)
 * Parsing records on each index (using recordParseSelectors and recordLinkSelector)
    config["recordParseSelectors"], config["recordLinkSelector"],
 * Record links should be sorted in athor list that named pages
 * Getting info from each page that pointed in recordLinks itemParseSelectors


Structure of vulnerabilities storage:
 * Indexes (from 1 to pages_count or enumerationSet)
 * Records (rows in indexed table)
 * Items (key-value set on each enumerated row)

EOF
