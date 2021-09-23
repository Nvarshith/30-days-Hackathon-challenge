n = int(input())
count=0
min=0
while n>=1:
    if n%2==1:
        count+=1
        n=n/2
        if count>=min:
            min=count
    else:
        count=0
        n=n/2
    
print(min)