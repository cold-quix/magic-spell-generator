#	
#	Filename:		spellgen.py
#	Programmer:		Jack Parkinson
#	First Version:	2021-03-06
#	Description:
#		A python script which randomly generates a magic spell, 
#		suitable for use in any fantasy-themed tabletop RPG.  Uses 
#		an SQL database to store spell attributes.
#		
#		
#		
#		
#		
#		
#		
#		
#	

# Import statements
import random
from random import choice
import mysql.connector
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


# Determine what system to use, generic by default
spellSystem = Ruleset.GENERIC.value;

if (len(sys.argv)) > 1:
	if (sys.argv[1] == Ruleset.DND_5.value):
		spellSystem = Ruleset.DND_5.value;
		
	if (sys.argv[1] == Ruleset.PATHFINDER_1.value):
		spellSystem = Ruleset.PATHFINDER_1.value;
		

# Initialize SQL cursor, defaulting to generic
if spellSystem == Ruleset.DND_5.value:
	spellDB = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "password1234",
		database = Ruleset.DND_5_DB.value
	)
elif spellSystem == Ruleset.PATHFINDER_1.value:
	spellDB = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "password1234",
		database = Ruleset.PATHFINDER_1_DB.value
	)
else:
	spellDB = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "password1234",
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
	#randSelect = random.randint(0, len(itme);
	tempString = str(choice(item));
	tempString = tempString.strip("(),'");
	finalSpell.append(tempString);

# Output spell description
print("Element: " + finalSpell[0]);
print("Targets: " + finalSpell[1]);
print("Shape: " + finalSpell[2]);
print("Damage: " + finalSpell[3]);
print("Effect: " + finalSpell[4]);



