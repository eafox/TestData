#Trying to sort out what all these commands mean (and maybe figure out where i can get mine in)


awk '
/^>/ 
{printf("\n%s\n",$0);next; }  											#print newline, %s, newline (%s=$0 ?), go to next line
{ printf("%s",$0);}  													#print $0 as %s?
END {printf("\n");}' < $1 | 											#print newline at end from file $1
awk 'NR>1{ printf("%s",$0); 											#print string
	 n++; if(n%2==0) 													#if number is even
	 { printf("\n");} 													#print newline
	 else { printf("\t");} }' | 										#otherwise, tab
	 awk -v k=$3 														#not sure
	 '{s=x++<k?x-1:int(rand()*x);										#think this might be the randomization line
		 if(s<k)R[s]=$0}END												#if S is within the probability, R[s] equals the current sequence
		 {for(i in R)print R[i]}' | 									#print the chosen sequences
		 awk -F"\t" -v f="$2" 											#new awk command to format new file
		 '{print $1"\n"$2 > f}'											#print the sequence name, newline, sequence to the new file.

$1=Start File
$2=End File
$3=Number to choose

\t=tab
%s=string

/^>/=
NR>1=
n+=
-v=
x++= s=x then add 1
<k?=less than K...
x-1:int(rand()*x) = range from the initial x to whole number (random number * new x)
-F=
f=$2 (new output file, second in input)
	"$2" (new set of quotes breaks out of R)

First section:
Second section:
Third section: take output from previous command and print to new file

PROBLEM: the same ones are chosen every time (set seed somewhere)

One more point about the use of a dollar sign. In scripting languages like Perl and the various shells, a dollar sign means the word following is the name of the variable. Awk is different. The dollar sign means that we are refering to a field or column in the current line. 

Simpler version of above?
srand();bioawk -c fastx -v k=10 '{y=x++<k?x-1:int(rand()*x);if(y<k)a[y]=">"$name"\n"$seq}END{for(z in a)print a[z]}' 
need bioawk (NICE!)
But problem with seed
