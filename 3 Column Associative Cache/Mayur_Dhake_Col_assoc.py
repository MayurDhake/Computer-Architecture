print "read file: trace"
ip=open("trace","r")
a=ip.readlines() 
print "The length of trace"
print(len(a))
btrace=[]
for i in range(len(a)):
    btrace.append(bin(int(a[i][2:],16))[2:])     #First remove label "2_" and then remove "0b" while converting to binary
    btrace[i]=btrace[i].zfill(32)
     
cache={}
rehash_bit={}
for i in range(512):            
    hasht=(bin(i))[2:].zfill(9)     #Remove "0b"
    rehash_bit[hasht]=1             #Set rehash bit = 1
    cache[hasht]=0                 #cache is empty



hit=0
miss=0

for i in range(len(btrace)):
    index=btrace[i][19:28]
    tag=btrace[i][0:19]
    tag_a=tag+index[0]      #appending high order bit of index to tag
    if cache[index]==tag_a:
        hit=hit+1
        rehash_bit[index]=0

    else:
        if rehash_bit[index]==1:        #If Rehash_bit=1
            miss=miss+1                 
            cache[index]=tag_a          #Pull block from memory into 1st half of column
            rehash_bit[index]=0         
        else:
            if index[0]==0:
                index_2 ="1"+index[1:]   #Flip the highest bit to go to second column (+256)
            else:
                index_2 ="0"+index[1:]   #Flip the highest bit to go to first column (-256)


            rehash_bit[index]=1         
            if cache[index_2]==tag_a:
                hit=hit+1
                swap=cache[index_2]
                cache[index_2]=cache[index]
                cache[index]=swap
            else:
                miss=miss+1
                cache[index_2]=tag_a    #Pull block from memory into 2nd half of column
                swap=cache[index_2]
                cache[index_2]=cache[index]
                cache[index]=swap

access=hit+miss
print "The number of accesses:"
print access
print "The number of hits:"
print hit
print "The number of  miss:"
print miss
print "Miss rate (%):"
print (miss/float(access))*100

        

