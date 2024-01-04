# Problem Link : https://codeforces.com/contest/977/problem/D

n = int(input())
nums = list(map(int,input().split()))
s = set()
for num in nums:
    temp = num
    c = 0
    while temp%3==0:
        temp//=3
        c+=1
    s.add((num,c))
s_list = sorted(s,key = lambda x: (x[1], -x[0]), reverse = True)
res = [item[0] for item in s_list]
res = ' '.join(map(str, res))
print(res)