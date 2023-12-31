# 1
def solution(board):
    N, M = len(board), len(board[0])
    DP = [[0]*M for _ in range(N)]
    mx = 0
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
            mx = max(mx, DP[i][j])

    return mx**2


# 2
def solution(board):
    N, M = len(board), len(board[0])
    MN = min(N, M)
    answer = 0
    arr = set()

    def find(x, y, mn):
        nonlocal answer, arr
        cnt = 0

        for i in range(x, x + mn):
            for j in range(y, y + mn):
                if board[i][j] == 1:
                    cnt += 1

        if cnt == mn ** 2:
            answer = max(answer, cnt)
        else:
            for i in range(N):
                for j in range(M):
                    if i + mn - 1 <= N and j + mn - 1 <= M \
                            and mn > 1 and (i, j, mn - 1) not in arr:
                        arr.add((i, j, mn - 1))
                        find(i, j, mn - 1)

    for i in range(N):
        for j in range(M):
            if i + MN <= N and j + MN <= M and (i, j, MN) not in arr:
                arr.add((i, j, MN))
                find(i, j, MN)

    return answer
