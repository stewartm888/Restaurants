#python code to convert any xml file into a json object and write it to a new file.

import xmltodict
import pprint
import json

print("\n")
print("Welcome to XML to JSON converter")
print("\n")

xml_file = str(input("Type the XML file (including extension) to convert: "))

print("\n")

with open(xml_file) as fd:
	doc = xmltodict.parse(fd.read())

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.dumps(doc))


print("\n"*3)

json_file = str(input("Type .txt file to write json object: "))

with open(json_file,'w') as outfile:
		json.dump(doc,outfile)

