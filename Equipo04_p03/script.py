#!/usr/bin/python3
from Bio import SeqIO
import sys
cmdargs = str(sys.argv)
i = 0
c = 0
for seq_record in SeqIO.parse(str(sys.argv[1]), "fasta"):
	# output_line = '%s\t%i' % (seq_record.id, len(seq_record))
	i += len(seq_record)
	c += 1
print(i / c)

