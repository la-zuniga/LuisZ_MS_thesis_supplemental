# script to change headers to sp. name and bacteria taxonomy

import sys
import os
import re
import argparse

# make an argument parser object to load a args_fasta file
parser = argparse.ArgumentParser(description='Load a fasta file.')
parser.add_argument('-f', '--fasta', type=str, help='Input fasta file.')
parser.add_argument('-k', '--KO', type=str, help='Input KO number.')
parser.add_argument('-s', '--species', type=str, help='Input species name.')
parser.add_argument('-p', '--process', type=str, help='Input process name.')
parser.add_argument('-n', '--N_rxns', type=str, help='Input N_rxns file.')
args_fasta = parser.parse_args()
args_fasta = args_fasta.fasta
args_KO = parser.parse_args()
args_KO = args_KO.KO
args_species = parser.parse_args()
args_species = args_species.species
args_process = parser.parse_args()
args_process = args_process.process
args_N_rxns = parser.parse_args()
args_N_rxns = args_N_rxns.N_rxns

# load N_rxns.txt
args_N_rxns_file = open(args_N_rxns, 'r')
args_N_rxns = args_N_rxns_file.readlines()

# load the args_fasta file
args_fasta_file = open(args_fasta, 'r')
args_fasta = args_fasta_file.readlines()

# remove text after the # in the headers of the args_fasta file
for i in range(len(args_fasta)):
    args_fasta[i] = args_fasta[i].split('#')
    args_fasta[i] = args_fasta[i][0]

# split columns of N_rxns by comma
for i in range(len(args_N_rxns)):
   args_N_rxns[i] = args_N_rxns[i].split(',')


# storing node names and taxonomy in lists
node_names = []
taxonomy_kingdom = []
taxonomy_phylum = []
taxonomy_genus = []
for i in range(len(args_N_rxns)):
    node_names.append(args_N_rxns[i][0])
    taxonomy_kingdom.append(args_N_rxns[i][6])
    taxonomy_phylum.append(args_N_rxns[i][7])
    taxonomy_genus.append(args_N_rxns[i][8])

# remove line breaks from taxonomy_genus list
for i in range(len(taxonomy_genus)):
    taxonomy_genus[i] = taxonomy_genus[i].replace('\n', '')

# concatenate elements of node names and 2 taxonomy lists seperated by _
taxonomy = []
for i in range(len(taxonomy_kingdom)):
    taxonomy.append(node_names[i] + '_' + taxonomy_kingdom[i] + '_' + taxonomy_phylum[i])

# for each element in taxonomy, append species to the end
for i in range(len(taxonomy)):
    taxonomy[i] = taxonomy[i] + '_' + args_species + '\n'

# make a dictionary with node names as keys and taxonomy as values
node_taxonomy_dict = dict(zip(node_names, taxonomy))

# search args_fasta for node names and replace the header with taxonomy
for i in range(len(args_fasta)):
    for key in node_taxonomy_dict:
        if key in args_fasta[i]:
            args_fasta[i] = args_fasta[i].replace(args_fasta[i], '>' + node_taxonomy_dict[key])

# remove seqeuences and headers that contain the word EMPTY or Animals
for i in range(len(args_fasta)):
    if 'EMPTY' in args_fasta[i] or 'Animals' in args_fasta[i]:
        args_fasta[i] = ''

# remove duplicates from args_fasta
args_fasta = list(dict.fromkeys(args_fasta))


# write args_fasta to a new file called args_fasta_taxonomy_KO.args_fasta
args_fasta_taxonomy_KO_file = open(args_species + '_' + args_process + '_' + args_KO + '_taxonomy' + '.fasta', 'w')
for i in range(len(args_fasta)):
    args_fasta_taxonomy_KO_file.write(args_fasta[i])
args_fasta_taxonomy_KO_file.close()


