nums=[0,1,0,3,12]
zero=[]
non_zero=[]
for i in nums:
    if i==0:
        zero.append(i)
    else:
        non_zero.append(i) 
print(non_zero+zero)        
        
