A, B, C = map(int, input().split())
n = 0

if B >= C: print(-1)
else: print(int(A / (C - B) + 1))