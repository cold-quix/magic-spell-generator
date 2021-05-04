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
#		an SQL database to store spell attributes.
#	

# Import statements
import mysql.connector # must be the first import statement
import cgi
import cgitb
cgitb.enable();
from random import choice
import sys
from enum import Enum


# Initialize enums for system comparison
class Ruleset(Enum):
	GENERIC = "GENERIC"
	GENERIC_DB = "generic_attributes"
	DND_5 = "DND5e"
	DND_5_DB = "dnd5e_attributes"
	PATHFINDER_1 = "PF1e"
	PATHFINDER_1_DB = "pathfinder1e_attributes"

# Get form data
formValue = cgi.FieldStorage();
	
# Determine what system to use, generic by default
if (formValue["form_system"].value == Ruleset.DND_5.value):
	spellSystem = Ruleset.DND_5.value;
elif (formValue["form_system"].value == Ruleset.PATHFINDER_1.value):
	spellSystem = Ruleset.PATHFINDER_1.value
else:
	spellSystem = Ruleset.GENERIC.value;
		

# Initialize SQL cursor, defaulting to generic
if spellSystem == Ruleset.DND_5.value:
	spellDB = mysql.connector.connect(
		host = "localhost",
		user = "RemoteUser",
		password = "",
		database = Ruleset.DND_5_DB.value
	)
elif spellSystem == Ruleset.PATHFINDER_1.value:
	spellDB = mysql.connector.connect(
		host = "localhost",
		user = "RemoteUser",
		password = "",
		database = Ruleset.PATHFINDER_1_DB.value
	)
else:
	spellDB = mysql.connector.connect(
		host = "localhost",
		user = "RemoteUser",
		password = "",
		database = Ruleset.GENERIC_DB.value
	)
spellCursor = spellDB.cursor();
spellCursor.execute("SELECT ElementName FROM Element");
listHolder = spellCursor.fetchall();

# Create lists to hold spell attributes
listElements = [];
listTargets = [];
listShapes = [];
listDamage = [];
listEffects = [];

# Fill lists with SQL data
for item in listHolder:
	listElements.append(item);

spellCursor.execute("SELECT TargetValue FROM Target");
listHolder = spellCursor.fetchall();
for item in listHolder:
	listTargets.append(item);

spellCursor.execute("SELECT ShapeValue FROM Shape");
listHolder = spellCursor.fetchall();
for item in listHolder:
	listShapes.append(item);

spellCursor.execute("SELECT DamageValue FROM Damage");
listHolder = spellCursor.fetchall();
for item in listHolder:
	listDamage.append(item);

spellCursor.execute("SELECT EffectName FROM Effect");
listHolder = spellCursor.fetchall();
for item in listHolder:
	listEffects.append(item);

# List of lists for easier handling
listAttributes = [listElements, listTargets, listShapes, listDamage, listEffects];

# Prepare final spell
finalSpell = [];

for item in listAttributes:
	tempString = str(choice(item));
	tempString = tempString.strip("(),'");
	finalSpell.append(tempString);

# Output HTML page
print('''<html>
	<head>
		<title>Jack Parkinson - Magic Spell Generator</title>
		
		<!-- CSS -->
		<link rel="stylesheet" href="../../css/style.css">
		<link rel="stylesheet" href="../../css/spellgen.css">
        
	</head>
	
	
	<body>
		<!-- Alert for IE browsers -->
		<div name="IE_warning" id="ID-IE_warning" class="IE_alert"></div>
		
		<!-- Page wrapper to help anchor footer -->
		<div name="page_wrapper" id="ID-page_wrapper" class="page_wrap">

			
			<!-- Intro -->
			<div name="intro_wrapper" id="ID-intro_wrapper" class="intro_wrap">
				<div name="intro_name" id="ID-intro_name" class="intro_title">
					Spell Generator
				</div>
				
				<div name="intro_text_1" id="ID-intro_text_1" class="intro_desc">
					This application generates a magic spell with random effects for use in a tabletop RPG.
				</div>
				
				<div name="intro_text_2" id="ID-intro_text_2" class="intro_desc">
					More systems and features to come in the future.
				</div>
				  
			</div>
			
			<!-- Spell Output -->
			<div name="spell_output_wrapper" id="ID-spell_output_wrapper" class="spell_wrap">
				<div class="spell_attribute_grid">
					<div class="attribute_title attribute_content">
						Your randomly generated spell awaits you.  Cast as you will, wizard!
					</div>
					
					<div class="attribute_one attribute_content">
						Element: 
					</div>
					<div class="value_one attribute_content">''');
# Output spell description
print(finalSpell[0]);
print('''</div>
					
					<div class="attribute_two attribute_content">
						Targets: 
					</div>
					<div class="value_two attribute_content">''');
print(finalSpell[1]);
print('''</div>
					
					<div class="attribute_three attribute_content">
						Shape: 
					</div>
					<div class="value_three attribute_content">''');
print(finalSpell[2]);
print('''</div>
					
					<div class="attribute_four attribute_content">
						Damage: 
					</div>
					<div class="value_four attribute_content">''');
print(finalSpell[3]);
print('''</div>
					
					<div class="attribute_five attribute_content">
						Effect: 
					</div>
					<div class="value_five attribute_content">''');
print(finalSpell[4]);
print('''</div>
					
				</div>
			</div>
			
			<!-- Spell Output -->
			<div name="spell_output_wrapper" id="ID-spell_output_wrapper" class="spell_wrap">
			</div>''');

print('''<!-- Navigation -->
			<div name="spell_nav_wrapper" id="ID-spell_nav_wrapper" class="spell_nav_wrap">
				<div name="spellgen_grid" id="ID-spellgen_grid" class="spell_nav_grid">
					<div class="spell_one spellgen_format">
						<form name="form_generic" method="POST" action="./spellgen.py">
							<input name="form_system" id="ID-form_system" type="hidden" value="DND5e">
							<input name="submit_system" id="ID-submit_system" type="submit" value="Dungeons & Dragons 5th Edition" class="spellgen_link">
						</form>
					</div>
					
					<div class="spell_two spellgen_format">
						<form name="form_generic" method="POST" action="./spellgen.py">
							<input name="form_system" id="ID-form_system" type="hidden" value="PF1e">
							<input name="submit_generic" id="submit_generic" type="submit" value="Pathfinder 1st Edition" class="spellgen_link">
						</form>
					</div>
					
					<div class="spell_three spellgen_format">
						<form name="form_generic" method="POST" action="./spellgen.py">
							<input name="form_system" id="ID-form_system" type="hidden" value="generic">
							<input name="submit_generic" id="submit_generic" type="submit" value="Generic" class="spellgen_link" >
						</form>
					</div>
				</div>
				
			</div>
			
			<!-- Lines to prevent footer overlapping content. -->
			<br>
			
			<!-- Footer -->
			<footer>
				<div class="footer_grid">
					<div class="footer_grid_content footer_grid_one">
						<a href="../../index.html" class="footer_link">Home</a>
					</div>
					<div class="footer_grid_content footer_grid_two">
						<a href="../../projects.html" class="footer_link">Projects</a>
					</div>
					<div class="footer_grid_content footer_grid_three">
						<a href="../../media.html" class="footer_link">Media</a>
					</div>
					<div class="footer_grid_content footer_grid_four">
						<a href="../../contact.html" class="footer_link">Contact</a>
					</div>
					<div class="footer_grid_content footer_grid_five">
						<a href="../../blog.html" class="footer_link">Blog</a>
					</div>
				</div>	
			</footer>
		</div>
		
		<!-- Scripts -->
		<script src="../../js/script.js"></script>
		
	</body>

</html>''');