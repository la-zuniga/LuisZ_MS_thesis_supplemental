# script to make a presence absence table where rows are species and columns are genes #

import sys
import os
import argparse
import re

# making an argument parser object to load a provide a KO number
parser = argparse.ArgumentParser(description='Load a KO number.')
parser.add_argument('-k', '--KO', type=str, help='Input KO number.')
parser.add_argument('-p', '--process', type=str, help='Input process name.')
args_KO = parser.parse_args()
args_KO = args_KO.KO
args_process = parser.parse_args()
args_process = args_process.process

# putting the species names in a list #

sp_names = ["Acau1", "Acau2", "Acon1", "Acon2", "Acon3", "Acra1", "Aful2", "Ibir2", "Vrig3", "Wfilter1", "Wfilter2", "Wfilter3", "Xmut1", "Xmut2"]

# making a function to load a file #
def load_file(file):
    file = open(file, "r")
    file = file.readlines()
    return file

# loading the fasta files with species names,_pargs_process, and KO numbers #
Acau1 = load_file("Acau1" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Acau2 = load_file("Acau2" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Acon1 = load_file("Acon1" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Acon2 = load_file("Acon2" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Acon3 = load_file("Acon3" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Acra1 = load_file("Acra1" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Aful2 = load_file("Aful2" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Ibir2 = load_file("Ibir2" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Wfilter1 = load_file("Wfilter1" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Wfilter2 = load_file("Wfilter2" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Wfilter3 = load_file("Wfilter3" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Vrig3 = load_file("Vrig3" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Xmut1 = load_file("Xmut1" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")
Xmut2 = load_file("Xmut2" + "_" + str(args_process) + "_" + str(args_KO) + "_" + "taxonomy" ".fasta")

# making a function to make a dictionary #
def make_dict(file):
    dict = {}
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            line = line.split(" ")
            line = line[0]
            line = line.replace(">", "")
            dict[line] = 1
    return dict


# making dictionaries for each species #
Acau1_dict = make_dict(Acau1)
Acau2_dict = make_dict(Acau2)
Acon1_dict = make_dict(Acon1)
Acon2_dict = make_dict(Acon2)
Acon3_dict = make_dict(Acon3)
Acra1_dict = make_dict(Acra1)
Aful2_dict = make_dict(Aful2)
Ibir2_dict = make_dict(Ibir2)
Vrig3_dict = make_dict(Vrig3)
Wfilter1_dict = make_dict(Wfilter1)
Wfilter2_dict = make_dict(Wfilter2)
Wfilter3_dict = make_dict(Wfilter3)
Xmut1_dict = make_dict(Xmut1)
Xmut2_dict = make_dict(Xmut2)

# taking the keys from each dictionary and put them in a list #
Acau1_keys = list(Acau1_dict.keys())
Acau2_keys = list(Acau2_dict.keys())
Acon1_keys = list(Acon1_dict.keys())
Acon2_keys = list(Acon2_dict.keys())
Acon3_keys = list(Acon3_dict.keys())
Acra1_keys = list(Acra1_dict.keys())
Aful2_keys = list(Aful2_dict.keys())
Ibir2_keys = list(Ibir2_dict.keys())
Vrig3_keys = list(Vrig3_dict.keys())
Wfilter1_keys = list(Wfilter1_dict.keys())
Wfilter2_keys = list(Wfilter2_dict.keys())
Wfilter3_keys = list(Wfilter3_dict.keys())
Xmut1_keys = list(Xmut1_dict.keys())
Xmut2_keys = list(Xmut2_dict.keys())

# concatenating all the keys into one list #
all_keys = Acau1_keys + Acau2_keys + Acon1_keys + Acon2_keys + Acon3_keys + Acra1_keys + Aful2_keys + Ibir2_keys + Vrig3_keys + Wfilter1_keys + Wfilter2_keys + Wfilter3_keys + Xmut1_keys + Xmut2_keys

# making a tab deliminated file where all keys are columns and row_names are rows #
with open("presence_absence_table" + "_" + str(args_process) + "_" + str(args_KO) + ".txt", "w") as output:
    output.write("row_names\t" + "\t".join(all_keys) + "\n")
    for key in sp_names:
        output.write(key + "\t")
        for key2 in all_keys:
            if key2 in eval(key + "_keys"):
                output.write("1" + "\t")
            else:
                output.write("0" + "\t")
        output.write("\n")



