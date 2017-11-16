#!/bin/bash

#./subsample_se_fasta.sh s.fasta s_sub.fasta 100000
#http://userweb.eng.gla.ac.uk/umer.ijaz/bioinformatics/oneliners.html?#SUBSAMPLING

awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' < $1 | awk 'NR>1{ printf("%s",$0); n++; if(n%2==0) { printf("\n");} else { printf("\t");} }' | awk -v k=$3 '{s=x++<k?x-1:int(rand()*x);if(s<k)R[s]=$0}END{for(i in R)print R[i]}' | awk -F"\t" -v f="$2" '{print $1"\n"$2 > f}'



bioawk -c fastx -v k=10 '{y=x++<k?x-1:int(srand()*x);if(y<k)a[y]=">"$name"\n"$seq}END{for(z in a)print a[z]}' ../Data/CO1_test_HiSeq_150_length_Forward.fasta
