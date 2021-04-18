/*
FILE:			dnd5e_attributes.sql
PROGRAMMER:		Jack Parkinson
FIRST VERSION:	2020-04-18
DESCRIPTION:
	A creation script for the DB used in spell_generator.py.  This DB 
    contains spell attribute data which will be used to make a D&D5e 
    spell and display it to the user at runtime.
*/
/* Statements to destroy & create the database each time the script is run */
DROP DATABASE IF EXISTS dnd5e_attributes;
CREATE DATABASE IF NOT EXISTS dnd5e_attributes;

USE dnd5e_attributes;

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
	("Acid"), 
    ("Cold"),
    ("Fire"),
    ("Force"),
    ("Lightning"),
    ("Necrotic"),
    ("Poison"),
    ("Psychic"),
    ("Radiant"),
    ("Thunder")
;
INSERT INTO Target(TargetValue) VALUES
	("Self"), 
    ("Enemy"),
    ("1"),
    ("2 separate"),
    ("3 separate"),
    ("2 group"),
    ("3 group")
;
INSERT INTO Shape(ShapeValue) VALUES
	("Cone"), 
    ("Cube"),
    ("Cylinder"),
    ("Line"),
    ("Sphere")
;
INSERT INTO Damage(DamageValue) VALUES
	("1d6"), 
    ("2d6"),
    ("3d8"),
    ("4d8"),
    ("3d10"),
    ("4d12")
;
INSERT INTO Effect(EffectName) VALUES
	("Blinded"), 
    ("Charmed"),
    ("Deafened"),
    ("Frightened"),
    ("Grappled"),
    ("Incapacitated"),
    ("Invisible"),
    ("Paralyzed"),
    ("Petrified"),
    ("Poisoned"),
    ("Prone"),
    ("Restrained"),
    ("Stunned"),
    ("Unconscious")
;