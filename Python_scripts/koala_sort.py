# script to sort through a ghostKoala summary file and get KO id's for nitrogen metabolism (nitrogen cycle) proteins/enzymes
# importing modules
import sys
import os
import re
import argparse


# make an argument parser object to load a ghost koala summary file
parser = argparse.ArgumentParser(description='Load the ghost koala summary')
parser.add_argument('-d', '--data', type=str, help='Input thr ghost koala summary file')
args_data = parser.parse_args()
args_data = args_data.data

# load the data
koala_file = open(args_data)
koala_contents = koala_file.readlines()

# this function will pull nitrogen metabolism hits by looking at the KEGG category column and searching for '00910' which is KEGG's identifier for N metabolism
def N_rxns (data):
    out = []
    for line in data:
        columns = line.split(',')
        category = columns[2]
        if re.search(r'00910', category):
            out.append(line)
    return out

# using the function
N_metab = N_rxns(koala_contents)
# opening and writing all he entries to a file
N_rxns_file = open('N_rxns.txt','w')
for entry in N_metab:
    N_rxns_file.write(entry)


# this function will look for the denitrification enzyme KEGG ids for denitrification
def get_denitrification (data):
    out = []
    for line in data:
        if re.search(r'K00370', line):
            out.append(line)
        elif re.search(r'K00371', line):
            out.append(line)
        elif re.search(r'K00374', line):
            out.append(line)
        elif re.search(r'K02567', line): 
            out.append(line)
        elif re.search(r'K02568', line):
            out.append(line)
        elif re.search(r'K00368', line):
            out.append(line)
        elif re.search(r'K15864', line):
            out.append(line)
        elif re.search(r'K04561', line):
            out.append(line)
        elif re.search(r'K02376', line):
            out.append(line)
        elif re.search(r'K00376', line):
            out.append(line)
    return out

# using the new function
deN_enzymes = get_denitrification(N_metab)

# opening and writing the denitrification hits file
deN_enzymes_file = open('denitrification.txt','w')
for entry in deN_enzymes:
    deN_enzymes_file.write(entry)


# this function will look for the nitrogen fixation enzyme KEGG ids 
def get_Nfixation (data):
    out = []
    for line in data:
        if re.search(r'K02588', line):
            out.append(line)
        elif re.search(r'K02586', line):
            out.append(line)
        elif re.search(r'K02591', line):
            out.append(line)
        elif re.search(r'K00531', line): 
            out.append(line)
        elif re.search(r'K22896', line):
            out.append(line)
        elif re.search(r'K22897', line):
            out.append(line)
        elif re.search(r'K22898', line):
            out.append(line)
        elif re.search(r'K22899', line):
            out.append(line)
    return out

# using the new function
Nfix_enzymes = get_Nfixation(N_metab)

# opening and writing the denitrification hits file
Nfix_enzymes_file = open('N_fixation.txt','w')
for entry in Nfix_enzymes:
    Nfix_enzymes_file.write(entry)


# this function will look for the assimilatory nitrate reduction enzyme KEGG ids 
def ass_nitrate_red (data):
    out = []
    for line in data:
        if re.search(r'K00367', line):
            out.append(line)
        elif re.search(r'K10534', line):
            out.append(line)
        elif re.search(r'K00372', line):
            out.append(line)
        elif re.search(r'K00360', line): 
            out.append(line)
        elif re.search(r'K17877', line):
            out.append(line)
        elif re.search(r'K00366', line):
            out.append(line)
        elif re.search(r'K26139', line):
            out.append(line)
        elif re.search(r'K26138', line):
            out.append(line)
        elif re.search(r'K00361', line):
            out.append(line)
    return out

# using the new function
as_nitrate_red_enzymes = ass_nitrate_red(N_metab)

# opening and writing the assimilatory nitrate reduction hits file
ass_nitrate_red_enzymes_file = open('as_nitrate_red.txt','w')
for entry in as_nitrate_red_enzymes:
    ass_nitrate_red_enzymes_file.write(entry)

# this function will look for the dissimilatory nitrate reduction enzyme KEGG ids 
def dis_nitrate_red (data):
    out = []
    for line in data:
        if re.search(r'K00370', line):
            out.append(line)
        elif re.search(r'K00371', line):
            out.append(line)
        elif re.search(r'K00374', line):
            out.append(line)
        elif re.search(r'K02567', line): 
            out.append(line)
        elif re.search(r'K02568', line):
            out.append(line)
        elif re.search(r'K00362', line):
            out.append(line)
        elif re.search(r'K00363', line):
            out.append(line)
        elif re.search(r'K03385', line):
            out.append(line)
        elif re.search(r'K15876', line):
            out.append(line)
    return out

# using the new function
dis_nitrate_red_enzymes = dis_nitrate_red(N_metab)

# opening and writing the dissimilatory nitrate reduction hits file
dis_nitrate_red_enzymes_file = open('dis_nitrate_red.txt','w')
for entry in dis_nitrate_red_enzymes:
    dis_nitrate_red_enzymes_file.write(entry)

# this function will look for nitrification enzyme KEGG ids 
def get_nitrification (data):
    out = []
    for line in data:
        if re.search(r'K10944', line):
            out.append(line)
        elif re.search(r'K10945', line):
            out.append(line)
        elif re.search(r'K10946', line):
            out.append(line)
        elif re.search(r'K10535', line): 
            out.append(line)
        elif re.search(r'K00370', line):
            out.append(line)
        elif re.search(r'K00371', line): 
            out.append(line)
    return out

# using the new function
nitrification_enzymes = get_nitrification(N_metab)

# opening and writing the dissimilatory nitrate reduction hits file
nitrification_enzymes_file = open('nitrification.txt','w')
for entry in nitrification_enzymes:
    nitrification_enzymes_file.write(entry)

# this function will look for the annamox enzyme KEGG ids for annamox
def get_annamox (data):
    out = []
    for line in data:
        if re.search(r'K00368', line):
            out.append(line)
        elif re.search(r'K15864', line):
            out.append(line)
        elif re.search(r'K20932', line):
            out.append(line)
        elif re.search(r'K20933', line): 
            out.append(line)
        elif re.search(r'K20934', line):
            out.append(line)
        elif re.search(r'K20935', line):
            out.append(line)
    return out

# using the new function
annamox_enzymes = get_annamox(N_metab)

# opening and writing the annamox hits file
annamox_enzymes_file = open('annamox.txt','w')
for entry in annamox_enzymes:
    annamox_enzymes_file.write(entry)