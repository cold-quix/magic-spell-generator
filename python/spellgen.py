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

# Start
print("Generating spell . . .");


# Initialize lists
list_elements = ["Fire", "Wind", "Lightning", "Water"];
list_targets = ["1", "2", "3", "4"];
list_shapes = ["Bolt", "Beam", "Cone", "Blast"];
list_effects = ["Stun", "Slow", "Knocks down", "Disarms"];
list_lists = [list_elements, list_targets, list_shapes, list_effects];

# Prepare final spell
finalSpell = [];

# Randomly copy attributes to spell
count = 0;
while count < len(list_lists):
	randSelect = random.randint(0, 3);
	finalSpell.append(list_lists[count][randSelect]);
	count += 1;

# Output spell description
print("Element: " + finalSpell[0]);
print("Targets: " + finalSpell[1]);
print("Shape: " + finalSpell[2]);
print("Effect: " + finalSpell[3]);

# Output spell name







