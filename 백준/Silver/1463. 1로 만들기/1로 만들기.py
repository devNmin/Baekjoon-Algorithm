N = int(input())
dptbl = [0] * 1000001

for i in range(2,N+1):
    # 현재의 수에서 1을 빼는 경우
    dptbl[i] = dptbl[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dptbl[i] = min(dptbl[i], dptbl[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        dptbl[i] = min(dptbl[i], dptbl[i // 3] + 1)
else:
    print(dptbl[N])