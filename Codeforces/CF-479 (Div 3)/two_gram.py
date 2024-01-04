# Problem Link : https://codeforces.com/contest/977/problem/B

n = int(input())
s = str(input())
freq = {}
for i in range(len(s)-1):
    sub = s[i:i+2]
    if sub in freq:
        freq[sub]+=1
    else:
        freq[sub]=1
maxima = float("-infinity")
ans = ""
for key,value in freq.items():
    if value>maxima:
        maxima = value
        ans = key
        
print(ans)