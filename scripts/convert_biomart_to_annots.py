''' Converts gene data from Ensembl Biomart to JSON-formatted annotations'''

import json, random

annots = []

chrs = [
	"1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
	"11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
	"21", "22", "X", "Y"
]

file_name = "data/annotations/Homo_sapiens,_Ensembl_80.tsv"
file = open(file_name, "r").readlines()

for chr in chrs:
	annots.append({"chr": chr, "annots": []});

for line in file[1:]:

	columns = line.strip().split("\t")

	chr = columns[4]

	if chr not in chrs:
		# E.g. chrMT, alternate loci scaffolds
		continue

	if chr == "X":
		chr = 22
	elif chr == "Y":
		chr = 23
	else:
		chr = int(chr) - 1

	start = int(columns[0])
	stop = int(columns[1]) - start
	gene_symbol = columns[2]
	gene_type = columns[3]

	annot = [
		gene_symbol,
		start,
		stop,
		1 #gene_type
	]

	annots[chr]["annots"].append(annot)

annots = json.dumps(annots)
annots = '{"annots":' + annots + '}'

open("data/annotations/all_human_genes.json", "w").write(annots)
