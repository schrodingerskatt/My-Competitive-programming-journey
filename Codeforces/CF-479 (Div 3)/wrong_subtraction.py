# Problem Link : https://codeforces.com/contest/977/problem/A

n, k = map(int, input().split())
while(k):
    if n%10 != 0:
        n-=1
    else:
        n//=10
    k-=1
    
print(n)