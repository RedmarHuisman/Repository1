#!/usr/bin/env python
# This program takes a protein sequence and determines its molecular weight
# The look-up table is generated from a web page through a series of regular expression replacements
# Redmar Huisman s2025655 18-1-2017
AminoDict={ # this is a dictionary containing the molecular weight of the 20 amino acids where the program will pull the values from to calculate the molecular weight of the protein
'A':89.09,
'R':174.20,
'N':132.12,
'D':133.10,
'C':121.15,
'Q':146.15,
'E':147.13,
'G':75.07,
'H':155.16,
'I':131.17,
'L':131.17,
'K':146.19,
'M':149.21,
'F':165.19,
'P':115.13,
'S':105.09,
'T':119.12,
'W':204.23,
'Y':181.19,
'V':117.15,
'X':0.0,
'-':0.0,
'*':0.0 }

ProteinSeq="FDILSATFTYGNR" # this is the sequence of amino acids initially used
ProteinSeq= raw_input().upper() # this allows me to manually insert a sequence of amino acids
MolWeight=0 # this is the base value for the variable MolWeight

for AminoAcid in ProteinSeq: # this starts the for loop that pulls a value from the dictionary for each amino acid in the sequence
	print AminoAcid, AminoDict[AminoAcid] # This instructs the program to print each amino acid from the sequence with the corresponding weight
	MolWeight = MolWeight + AminoDict[AminoAcid] # this adds up the weight of all amino acids with the base value for MolWeight to calculate the molecular weight

print "Protein:", ProteinSeq # this prints the sequence of amino acids
print "Molecular weight: %.1f" % (MolWeight) # this prints the variable MolWeight as value with one number after the decimal point
