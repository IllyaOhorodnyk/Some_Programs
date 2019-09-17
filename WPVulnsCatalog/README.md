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
 * * pageParseSelectors; # Internal dictionary of name elements that need extract and CSS selector that extracts it
 * * parserProtectionBypass; # Can be name of func


Procedure of parsing:
 * Create indexes (enumerable object that contain list of values for enumerationOption parameter)
    config["enumerationOption"], config["enumerationSet"], config["pagesCountSelector"] ==> {INDEXATION} ==> indexes(context protected)
 * Parsing records on each index
    config["recordParseSelectors"], config["recordLinkSelector"], indexes ==> {RECORDS_PARSE} ==> records(context protected), pages_links(is a part of records)
 * Parsing each page that pointed in pages list
    config["pageParseSelectors"], pages_links ==> {PAGES_PARSE} ==> pages(context protected)

Context protection implemets: # Context implement on each entity differently
  * List of contextes:
  * * Resource
  * * Indexes
  * * Records
  * * Pages
  * Resource:
  * * This hold any info about state of resource
  * Indexes:
  * * This hold values that describe in recordParseSelector
  * Pages:
  * * This hold values that describe in pageParseSelector


Structure of vulnerabilities storage:
 * Records (rows in indexed table)
 * Pages (key-value set on each enumerated row)

EOF
