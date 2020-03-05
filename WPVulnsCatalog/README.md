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

Modules:
* Parser
* Control plane
* Data source

Entities for the Parser:
* Vulnerability
* Resourse
* Index
* Configuration
* Selector
* Bypass
* Context

Description:
* Vulnerability:
* * This class describe Vulnerability object with link to the Index and the Resourse
* Resourse:
* * This class describe Resourse object with flexible parse method that depends on configuration
* Index:
* * This class represents remote page that hold information about vulnerabiility/link to the next Index and inforation that explain how to parse it
* Configuration:
* * This class describe Configuration for specific resourse: Selectors for each Index, code for Bypass, Bundle of Index, Selector for page with vulnerability
* Selector:
* * This class describe Selector that desribe how and what extract information from Index
* Bypass:
* * This class describe how to bypass parse protection of the Resourse. Can use for whole resourse. Based on python's decorators mechanism.
* Context:
* * This class provide protected dictionary. Protect mechanism can be different for each use.

EOF
