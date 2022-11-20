file=open("sequence.txt","r")
r=file.read()
size=len(r)
score_A=0
score_C=0
score_T=0
score_G=0
for i in range(size):
    if(r[i]=='A' or r[i]=='a'):
        score_A+=1
    elif (r[i]=='C'or r[i]=='c'):
        score_C+=1
    elif (r[i]=='T' or r[i]=='t'):
        score_T+=1
    elif (r[i]=='G'or r[i] =='g'):
        score_G+=1
print("score of A is", score_A)
print("score of C is", score_C)
print("score of T is", score_T)
print("score of G is", score_G) 


output:
>
score of A is 416
score of C is 203
score of T is 407
score of G is 140