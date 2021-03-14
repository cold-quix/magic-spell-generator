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
import random
import mysql.connector

# Start
print("Generating spell . . .");

# Initialize SQL cursor
spellDB = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "password1234",
	database = "spell_attributes"
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
	randSelect = random.randint(0, 3);
	tempString = str(item[randSelect]);
	tempString = tempString.strip("(),'");
	finalSpell.append(tempString);

# Output spell description
print("Element: " + finalSpell[0]);
print("Targets: " + finalSpell[1]);
print("Shape: " + finalSpell[2]);
print("Damage: " + finalSpell[3]);
print("Effect: " + finalSpell[4]);



