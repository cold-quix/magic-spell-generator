/*
FILE:			spell_attributes.sql
PROGRAMMER:		Jack Parkinson
FIRST VERSION:	2020-03-07
DESCRIPTION:
	A creation script for the DB used in spell_generator.py.  This DB 
    contains spell attribute data which will be used to make a random 
    spell and display it to the user at runtime.
*/
/* Statements to destroy & create the database each time the script is run */
DROP DATABASE IF EXISTS spell_attributes;
CREATE DATABASE IF NOT EXISTS spell_attributes;

USE spell_attributes;

/*
==============
Table Creation
==============
*/
/*
Element
An element has its own ID and a name which describes what 
element the spell will use.
*/
CREATE TABLE Element(
	Element_ID INT AUTO_INCREMENT NOT NULL,
    ElementName VARCHAR(50) NOT NULL,
    
    PRIMARY KEY (Element_ID)
);

/*
Target
A target has its own ID, and a value which describes 
the number of targets a spell can hit.
*/
CREATE TABLE Target(
	Target_ID INT AUTO_INCREMENT NOT NULL,
    TargetValue VARCHAR(50) NOT NULL,
    
    PRIMARY KEY (Target_ID)
);

/*
Shape
A shape has its own ID and a value which describes 
the shape a spell will be projected in.
*/
CREATE TABLE Shape(
	Shape_ID INT AUTO_INCREMENT NOT NULL,
    ShapeValue VARCHAR(50) NOT NULL,
    
    PRIMARY KEY (Shape_ID)
);

/*
Damage
A damage entry has its own ID and a value which describes
the amount of damage the spell will deal.  These values 
are intentionally vague so they work with many tabletop 
systems.
*/
CREATE TABLE Damage(
	Damage_ID INT AUTO_INCREMENT NOT NULL,
    DamageValue VARCHAR(50) NOT NULL,
    
    PRIMARY KEY (Damage_ID)
);

/*
Effect
An effect has its own ID and a name which describes 
the effects 
*/
CREATE TABLE Effect(
	Effect_ID INT AUTO_INCREMENT NOT NULL,
    EffectName VARCHAR(50) NOT NULL,
    
    PRIMARY KEY (Effect_ID)
);

/*
==============
Data Insertion
==============
*/
INSERT INTO Element(ElementName) VALUES
	("Lightning"), 
    ("Fire"),
    ("Water"),
    ("Wind"),
    ("Earth"),
    ("Ice"),
    ("Metal"),
    ("Light"),
    ("Shadow"),
    ("Energy"),
    ("Poison")
;
INSERT INTO Target(TargetValue) VALUES
	("1"), 
    ("2"),
    ("3"),
    ("4"),
    ("Self"),
    ("Nearest enemy"),
    ("Farthest enemy"),
    ("All enemies"),
    ("Nearest ally"),
    ("Farthest ally"),
    ("All allies")
;
INSERT INTO Shape(ShapeValue) VALUES
	("Bolt"), 
    ("Beam"),
    ("Cone"),
    ("Blast"),
    ("Cloud"),
    ("Cyclone"),
    ("Arcing chain"),
    ("Wall"),
    ("Trap"),
    ("Caster sculpt"),
    ("Puppeteered orb")
;
INSERT INTO Damage(DamageValue) VALUES
	("None"), 
    ("Low"),
    ("Medium"),
    ("High"),
    ("Damage over time"),
    ("Short delay"),
    ("Medium delay"),
    ("Long delay"),
    ("Slight elemental weakness"),
    ("Medium elemental weakness"),
    ("High elemental weakness")
;
INSERT INTO Effect(EffectName) VALUES
	("Stun"), 
    ("Slow"),
    ("Tumble"),
    ("Disarm"),
    ("Blind"),
    ("Confuse"),
    ("Charm"),
    ("Cripple"),
    ("Amnesia"),
    ("Terrify"),
    ("Sleep")
;