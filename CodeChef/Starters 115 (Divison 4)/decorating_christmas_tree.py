# Problem Link : https://www.codechef.com/START115D/problems/CHRISDECOR

t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    ans1 = x // 2 + min(x % 2, y // 3)
    ans2 = min(x, y // 3)
    ans3 = ans2 + (x - ans2) // 2
    if(n<=max(ans1,ans3)):
        print("YES")
    else:
        print("NO")