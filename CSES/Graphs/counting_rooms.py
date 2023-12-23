n, m = map(int, input().split())
a = []
for i in range(n):
    row = list(map(str, input().strip()))
    a.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(i, j):
    visited[i][j]=True
    for dr, dc in directions:
        r, c = i + dr, j + dc
        if 0 <= r < n and 0 <= c < m and visited[r][c]==False and a[r][c] == '.':
            dfs(r, c)

count = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == '.' and visited[i][j]==False:
            dfs(i, j)
            count += 1

print(count)