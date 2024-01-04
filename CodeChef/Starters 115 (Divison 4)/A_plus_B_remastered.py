# Problem Link : https://www.codechef.com/START115D/problems/APLUSB

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    B = sorted(B)
    C = []
    for i in range(n):
        C.append(A[i] + B[i])
    Flag = True
    for i in range(0, n-1):
        if C[i] != C[i+1]:
            Flag = False
            break
    if not Flag:
        print(-1)
    else:
        for elem in A:
            print(elem, end=" ")
        print()
        for elem in B:
            print(elem, end=" ")
        print()

