N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:(x[0],x[1]))
for x,y in arr:
    print(x,y)