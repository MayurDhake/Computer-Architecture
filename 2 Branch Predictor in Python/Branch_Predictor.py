print "read file"
ip=open("hwtrace.out","r")
a=[]
a=ip.readlines()

#c=0
#while c<len(a):
 #   print a[c]
  #  c=c+1

len_a =len(a)
print len_a

c=0
b=[]
while c<len_a-1:
    z=((int(a[c+1],16))-(int(a[c],16)))
    if z>15 or z<0:
        b.append(a[c])
        #print z
    c=c+1

#print "b"
#c=0
#while c<len(b):
 #   print b[c]
  #  c=c+1

    
  
#remove duplicate
def uniq(b):
    op=[]
    p=0
    for p in b:
        if p not in op:
            op.append(p)
    return op
unq_b = []
unq_b=uniq(b)
print "dupli"


c=0
while c<len(unq_b):
    print unq_b[c]
    c=c+1

# dictoinary
branch_one={}
i=0

for i in range(len(unq_b)):
    pivot=(bin(int(unq_b[i],16))[-5:])
    branch_one[pivot]=1

print branch_one

#comparisons
hit=0
miss=0
for i in range((len_a)-1):
    for j in range(len(unq_b)):
        q=int(a[i+1],16)-int(a[i],16)
        if unq_b[j]==a[i]:
            pivot=bin(int(a[i],16))[-5:]
            if(q>15 or q<0):
                if branch_one[pivot]==1:
                    hit=hit+1
                else:
                    miss=miss+1
                    branch_one[pivot]=1
            else:
                if branch_one[pivot]==0:
                    hit=hit+1
                else:
                    miss=miss+1
                    branch_one[pivot]=0


print "predictions"
print hit

print "mispredictions"
print miss

total = hit+miss
accuracy=float(hit*100/float(total))

print "One bit Predictor accuracy"
print accuracy
        
    
#################################

##2 bit predictor


# dictoinary
branch_two={}
i=0

for i in range(len(unq_b)):
    pivot=(bin(int(unq_b[i],16))[-4:])
    branch_two[pivot]=1

print branch_two

#comparisons
hit=0
miss=0
for i in range((len_a)-1):
    for j in range(len(unq_b)):
        q=int(a[i+1],16)-int(a[i],16)
        if unq_b[j]==a[i]:
            pivot=bin(int(a[i],16))[-4:]
            if(q>15 or q<0):
                if branch_two[pivot]==0:
                    miss=miss+1
                    branch_two[pivot]=1
                elif branch_two[pivot]==1:
                    miss=miss+1
                    branch_two[pivot]=3
                elif branch_two[pivot]==2:
                    hit=hit+1
                    branch_two[pivot]=3
                elif branch_two[pivot]==3:
                    hit=hit+1
            else:
                if branch_two[pivot]==0:
                    hit=hit+1
                elif branch_two[pivot]==1:
                    hit=hit+1
                    branch_two[pivot]=0
                elif branch_two[pivot]==2:
                    miss=miss+1
                    branch_two[pivot]=0
                elif branch_two[pivot]==3:
                    miss=miss+1
                    branch_two[pivot]=2
                    

print "Dictionary"
print branch_two

print "predictions"
print hit

print "mispredictions"
print miss


total = hit+miss
accuracy=float(hit*100/float(total))

print "Two Bit Predictor accuracy"
print accuracy


############################################

## 3 bit predictor



# dictoinary
branch_3={}
i=0

for i in range(len(unq_b)):
    pivot=(bin(int(unq_b[i],16))[-3:])
    branch_3[pivot]=1

print branch_3

#comparisons
hit=0
miss=0
for i in range((len_a)-1):
    for j in range(len(unq_b)):
        q=int(a[i+1],16)-int(a[i],16)
        if unq_b[j]==a[i]:
            pivot=bin(int(a[i],16))[-3:]
            if(q>15 or q<0):
                if branch_3[pivot]==0:
                    miss=miss+1
                    branch_3[pivot]=1
                elif branch_3[pivot]==1:
                    miss=miss+1
                    branch_3[pivot]=2
                elif branch_3[pivot]==2:
                    miss=miss+1
                    branch_3[pivot]=3
                elif branch_3[pivot]==3:
                    miss=miss+1
                    branch_3[pivot]=7
                if branch_3[pivot]==4:
                    hit=hit+1
                    branch_3[pivot]=5
                elif branch_3[pivot]==5:
                    hit=hit+1
                    branch_3[pivot]=6
                elif branch_3[pivot]==6:
                    hit=hit+1
                    branch_3[pivot]=7
                elif branch_3[pivot]==7:
                    hit=hit+1
                
            else:
                if branch_3[pivot]==0:
                    hit=hit+1
                elif branch_3[pivot]==1:
                    hit=hit+1
                    branch_3[pivot]=0
                elif branch_3[pivot]==2:
                    hit=hit+1
                    branch_3[pivot]=1
                elif branch_3[pivot]==3:
                    hit=hit+1
                    branch_3[pivot]=2
                if branch_3[pivot]==4:
                    miss=miss+1
                    branch_3[pivot]=0
                elif branch_3[pivot]==5:
                    miss=miss+1
                    branch_3[pivot]=4
                elif branch_3[pivot]==6:
                    miss=miss+1
                    branch_3[pivot]=5
                elif branch_3[pivot]==7:
                    miss=miss+1
                    branch_3[pivot]=6
               
                    
print "Dictionary"
print branch_3

print "predictions"
print hit

print "mispredictions"
print miss


total = hit+miss
accuracy=float(hit*100/float(total))

print "3 Bit Predictor accuracy"
print accuracy


