for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 1 다음에 2가 왔을 때!
    # 열 별로 보는게 좋을듯 : 열 우선 순회
    cnt = 0
    for j in range(n):
        for i in range(n):
            # 만약에 1(n)이 있다면, 이 다음에 2(s)를 만나면 교착상태
            if arr[i][j] == 1:
            # 다음에 오는 친구가 2여야함
            # 1을 만나면 카운팅이 되지 않기 때문에 멈추기
                for k in range(i+1, n): # 다음부터 열 끝까지
                    if arr[k][j] == 1: # 1을 만나면 멈추기
                        break
                    elif arr[k][j] == 2: # 2를 만나면 더해주고 멈추기
                        cnt += 1
                        break

    print(f'#{tc} {cnt}')
