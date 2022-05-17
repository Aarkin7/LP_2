#include <bits/stdc++.h>
#define N 8
using namespace std;

bool safe(int row, int col, int board[N][N], int rowLook[N], int slash[N][N], int back[N][N], int slashlook[], int backlook[]) {
	if (rowLook[row] == 1 || slashlook[slash[row][col]] == 1 || backlook[back[row][col]] == 1) {
		return false;
	}
	return true;
}

bool find(int col, int board[N][N], int rowLook[N], int slash[N][N], int back[N][N], int slashlook[], int backlook[]) {
	if (col >= N) {
		return true;
	}

	for (int i = 0; i < N; i++) {
		if (safe(i, col, board, rowLook, slash, back, slashlook, backlook)) {
			board[i][col] = 1;
			rowLook[i] = 1;
			slashlook[slash[i][col]] = 1;
			backlook[back[i][col]] = 1;

			bool sub = find(col + 1, board, rowLook, slash, back, slashlook, backlook);

			if (sub) {
				return true;
			}

			board[i][col] = 0;
			rowLook[i] = 0;
			slashlook[slash[i][col]] = 0;
			backlook[back[i][col]] = 0;

		}
	}

	return false;
}

void solve() {

	int board[N][N], slash[N][N], back[N][N];
	int rowLook[N];

	int slashlook[2 * N - 1], backlook[2 * N - 1];

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			board[i][j] = 0;
			slash[i][j] = i + j;
			back[i][j] = i - j + N - 1;
		}
	}

	for (int i = 0; i < 2 * N - 1; i++) {
		slashlook[i] = 0;
		backlook[i] = 0;
	}

	for (int i = 0; i < N; i++) {
		rowLook[i] = 0;
	}


	bool ans = find(0, board, rowLook, slash, back, slashlook, backlook);

	if (ans) {
		cout << "YES\n";
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cout << board[i][j] << " ";
			}
			cout << endl;
		}
	} else {
		cout << "NO\n";
	}
}

int main() {

	solve();

	return 0;
}


// TC: O(N!) N factorial


