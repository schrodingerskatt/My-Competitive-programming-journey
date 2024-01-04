# Problem Link : https://www.codechef.com/START115D/problems/CHOCDISTRIB


t = int(input())

for _ in range(t):
    n = int(input())
    if(n == 1):
        print("1"+" 1")
    else:
        if(n%2==1):
            m = (n//2)+1 
        else:
            m = (n//2)
        print(str(m)+" "+str(n))