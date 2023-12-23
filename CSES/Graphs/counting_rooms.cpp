#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<vector<char>> a;
vector<vector<bool>> visited;
vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

void dfs(int i, int j) {
    visited[i][j] = true;
    for (const auto& d : directions) {
        int r = i + d.first;
        int c = j + d.second;
        if (0 <= r && r < n && 0 <= c && c < m && !visited[r][c] && a[r][c] == '.') {
            dfs(r, c);
        }
    }
}

int main() {
    cin >> n >> m;
    a.resize(n, vector<char>(m));
    visited.resize(n, vector<bool>(m, false));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    int count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == '.' && !visited[i][j]) {
                dfs(i, j);
                count++;
            }
        }
    }

    cout << count << endl;

    return 0;
}
