#!/usr/bin/python3
print("Content-type: text/html\n\n");
# The above two lines are boilerplate to ensure no print statements cause 
# problems later in the program.

#	
#	Filename:		spellgen.py
#	Programmer:		Jack Parkinson
#	First Version:	2021-03-06
#	Description:
#		A python script which randomly generates a magic spell, 
#		suitable for use in any fantasy-themed tabletop RPG.  Uses 
#		a flat .txt file database to store spell attributes.
#	

# Import statements
import cgi;
import random;

# If no selection, output default page
form = cgi.FieldStorage();
editionChoice = form.getvalue("edition");

if (editionChoice == None or editionChoice == "default"):
	# print default page
	# Output header
	fs = open("./spellgenStatic/MSGnode1head.html", "r");
	tempData = fs.read();
	print(tempData);
	fs.close();

	# Output selector
	fs = open("./spellgenStatic/MSGnode2body.html", "r");
	tempData = fs.read();
	print(tempData);
	fs.close();
	
	# End of page
	fs = open("./spellgenStatic/MSGnode3footer.html", "r");
	tempData = fs.read();
	print(tempData);
	fs.close();
else:
	# print page with spell table
	# Output header
	fs = open("./spellgenStatic/MSGnode1head.html", "r");
	tempData = fs.read();
	print(tempData);
	fs.close();

	# Output selector
	fs = open("./spellgenStatic/MSGnode2body.html", "r");
	tempData = fs.read();
	print(tempData);
	fs.close();

	# Output spell table
	# Start table to hold spell output
	tempData = '''<div name="spell_wrapper" id="ID-spell_wrapper" class="spell_wrap">
				<table class="spell_table">''';
	print(tempData);
	# Read data from text files and parse randomly
	fileSuffixes = ["type","target","shape","damage","effect"];
	for suffix in fileSuffixes:
		CSVFile = "./spellgenData/" + editionChoice + "_" + suffix + ".txt";
		fs = open(CSVFile, "r");
		tempData = fs.read();
		tempData = tempData.split(",");
		print("<tr><td>" + suffix + "</td><td>" + tempData[random.randint(0, len(tempData)-1)] + "</td></tr>");
	# Close table and page wrapper div
	print("</table>");
	print("</div>");

	# End of page
	fs = open("./spellgenStatic/MSGnode3footer.html", "r");
	tempData = fs.read();
	print(tempData);
	fs.close();


