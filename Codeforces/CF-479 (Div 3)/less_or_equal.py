# Problem Link : https://codeforces.com/contest/977/problem/C

n, k = map(int, input().split())
seq = input_list = list(map(int, input().split()))
seq.sort()


if k == 0 and seq[0]>1:
    print(1)
elif k == 0 and seq[0]==1:
    print(-1)
elif k <= n-1:
    if seq[k-1]!=seq[k]:
        print(seq[k-1])
    else:
        print(-1)
elif k == n:
    print(seq[n-1])