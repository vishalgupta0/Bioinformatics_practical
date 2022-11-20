def solve_fingerprint(seq_list, no_of_col):
    seq_dict=dict()
    for column in range(no_of_col):
        counta, countc, countt, countg=0,0,0,0
        for colseq in seq_list:
            if colseq[column]=='A':
                counta+=1
            elif colseq[column]=='C':
                countc+=1
            elif colseq[column]=='T':
                countt+=1
            elif colseq[column]=='G':
                countg+=1
        seq_dict[column]=[counta, countc, countt, countg]
    display_results(seq_dict)

def display_results(seq_dict):
    print("\tA \tC \tT \tG")
    for key in seq_dict:
        print("\n",*seq_dict[key],sep="\t")

no_of_seq=int(input("Enter the number of sequence: "))
print("Enter all the sequences")
seq_list=[]
for _ in range(no_of_seq):
    seq_list.append(list(map(str, input("").split())))
solve_fingerprint(seq_list, len(seq_list[0]))


output:
>
Enter the number of sequence: 3
Enter all the sequences
A C T G A T G 
A T C A G A A
A T A A G C A
	A 	C 	T 	G

	3	0	0	0

	0	1	2	0

	1	1	1	0

	2	0	0	1

	1	0	0	2

	1	1	1	0

	2	0	0	1