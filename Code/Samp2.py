#!/usr/bin/python

"""Subsample fasta file(s) [one unpaired or set of paired] to new file with specified number of sequences """

___author__ = "Emma Fox (eafox@ucla.edu)"
__version__ = "0.0.1"

########################################################################
# IMPORTS                                                              #
########################################################################
import sys
import os
import argparse
from Bio import SeqIO
import random

########################################################################
# ARGUMENTS                                                            #
########################################################################
parser = argparse.ArgumentParser(description="Sample fasta file with replacement")
parser.add_argument("numSeq", type=int, help="Specify the number of sequences for the new file. Integer. No tag needed")
#There will be less if it runs out of space from the replicating?
parser.add_argument("--setSeed", type=int, nargs="?", help="Specify a seed for this set of files")
parser.add_argument("--totalLen", type=int, nargs="?", help="Specify total number of sequences in new file (if different from numSeq")
parser.add_argument("--maxCopy", type=int, nargs="?", help="Specify the maximum possible numbers of copies of one sequence")
parser.add_argument("--datFile", type=str, help="Name of unpaired fasta file. Cannot be used with --F_datFile or --R_datFile.")
parser.add_argument("--F_datFile", type=str, help="Name of forward paired fasta file. Must be used with same length --R_datFile.")
parser.add_argument("--R_datFile", type=str, help="Name of reverse paired fasta file. Must be used with same length --F_datFile.")
parser.add_argument("--outPref", type=str, help="Optional prefix for output file")
args = parser.parse_args()

########################################################################
# ERROR MESSAGES                                                       #
########################################################################
if args.outPref:
	outName="%s.fasta" % (args.outPref)
	F_outName="%s_F.fasta" % (args.outPref)
	R_outName="%s_R.fasta" % (args.outPref)
else:
	outName="samp.fasta"
	F_outName="samp_F.fasta" 
	R_outName="samp_R.fasta" 

if args.datFile:
	if args.F_datFile:
		parser.print_help()
		sys.exit(1)
	elif args.R_datFile:
		parser.print_help()
		sys.exit(1)
	else:
		print("\nInput File: {}".format(args.datFile))
		print("Output File: {}".format(outName))
		
if args.F_datFile:
	if args.R_datFile:
		if len(args.F_datFile)==len(args.R_datFile):
			print("\nForward Input File: {}".format(args.F_datFile))
			print("Forward Output File: {}".format(F_outName))
			print("Reverse Input File: {}".format(args.R_datFile))
			print("Reverse Output File: {}".format(R_outName))
		elif len(args.F_datFile)!=len(args.R_datFile):
			parser.print_help()
			sys.exit(1)
	else:
		parser.print_help()
		sys.exit(1)

if args.setSeed is None:
    args.setSeed = int(1)
if args.totalLen is None:
    args.totalLen = args.numSeq
if args.maxCopy is None:
    args.maxCopy = 10

print("Number of Unique Output Sequences: {}".format(args.numSeq))
print("Total Number of Sequences: {}".format(args.totalLen))
print("Seed: {}\n".format(args.setSeed))

copySeed=random.randint(1,1000000)

########################################################################
# FUNCTIONS                                                            #
########################################################################
if args.datFile:
	newFile=open(outName,"w")
	newFile.close()
	with open(args.datFile) as inFile, open(outName, 'a') as outFile:
		seqs = SeqIO.parse(inFile, "fasta")
		random.seed(args.setSeed)
		subSamp = ((seq.name, seq.seq) for seq in random.sample(list(seqs), args.numSeq))
		crntLen=0
		for newSeq in subSamp:
			crntLen=crntLen+1
			outFile.writelines(">{}\n{}\n".format(*newSeq))
			if args.totalLen!=args.numSeq:
				random.seed(copySeed)
				copyNum=random.randint(1,args.maxCopy)
				oldLen=crntLen
				crntLen=crntLen+1*copyNum
				if crntLen<args.totalLen:
					for i in range(0,copyNum):
						outFile.writelines(">{}\n{}\n".format(*newSeq))
				if crntLen>args.totalLen:
					for i in range(0,args.totalLen-oldLen-1):
						outFile.writelines(">{}\n{}\n".format(*newSeq))	

			
if args.F_datFile:
	newFile=open(F_outName,"w")
	newFile.close()
	with open(args.F_datFile) as inFile, open(F_outName, 'a') as outFile:
		seqs = SeqIO.parse(inFile, "fasta")
		random.seed(args.setSeed)
		subSamp = ((seq.name, seq.seq) for seq in random.sample(list(seqs), args.numSeq))
		crntLen=0
		for newSeq in subSamp:
			crntLen=crntLen+1
			outFile.writelines(">{}\n{}\n".format(*newSeq))
			if args.totalLen!=args.numSeq:
				random.seed(copySeed)
				copyNum=random.randint(1,args.maxCopy)
				oldLen=crntLen
				crntLen=crntLen+1*copyNum
				if crntLen<args.totalLen:
					for i in range(0,copyNum):
						outFile.writelines(">{}\n{}\n".format(*newSeq))
				if crntLen>args.totalLen:
					for i in range(0,args.totalLen-oldLen-1):
						outFile.writelines(">{}\n{}\n".format(*newSeq))	

if args.R_datFile:
	newFile=open(R_outName,"w")
	newFile.close()
	with open(args.R_datFile) as inFile, open(R_outName, 'a') as outFile:
		seqs = SeqIO.parse(inFile, "fasta")
		random.seed(args.setSeed)
		subSamp = ((seq.name, seq.seq) for seq in random.sample(list(seqs), args.numSeq))
		crntLen=0
		for newSeq in subSamp:
			crntLen=crntLen+1
			outFile.writelines(">{}\n{}\n".format(*newSeq))
			if args.totalLen!=args.numSeq:
				random.seed(copySeed)
				copyNum=random.randint(1,args.maxCopy)
				oldLen=crntLen
				crntLen=crntLen+1*copyNum
				if crntLen<args.totalLen:
					for i in range(0,copyNum):
						outFile.writelines(">{}\n{}\n".format(*newSeq))
				if crntLen>args.totalLen:
					for i in range(0,args.totalLen-oldLen-1):
						outFile.writelines(">{}\n{}\n".format(*newSeq))	
		
