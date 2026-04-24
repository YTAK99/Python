# Dynamic Programming
# memorization
# 피보나치수열

# 3
# 26 40 83
# 49 60 57
# 13 89 99


#         R             G                 B
# 1       26            40                83
# 2   (40+49=89)      (26+60=86)         (26+57=83)
# 3   (83+13=96)      (83+89=172)        (86+99=185)

#1. ############################################################################################################


n = int(input())
# print(n)
r, g, b = map(int, input().split())

for x in range(n - 1):
    nr, ng, nb = map(int, input().split())
    
    r, g, b = nr + min(g, b), ng + min(r, b), nb + min(r, g)

print(min(r, g, b))

#2. ############################################################################################################


import sys
N = int(sys.stdin.readline().strip())
R = G = B = 0

for t in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    if t == 0:
        R, G, B = r, g, b
    else:
        n_R = r + min(G, B)
        n_G = g + min(R, B)
        n_B = b + min(R, G)
        R, G, B = n_R, n_G, n_B
print(min(R, G, B))


#3. ############################################################################################################


R = []; G = []; B = []
crdR = []; crdG = []; crdB = []
N = int(input())
for x in range(N):
    r, g, b = map(int, input().split())
    R.append(r)
    G.append(g)
    B.append(b)

crdR = R.copy()
crdG = G.copy()
crdB = B.copy()

# print(f"crdRGB -----")
# for x in range(N):
#     print(crdR[x], crdG[x], crdB[x])

for x in range(1, N):
    crdR[x] = R[x] + min(crdG[x-1], crdB[x-1])
    crdG[x] = G[x] + min(crdR[x-1], crdB[x-1])
    crdB[x] = B[x] + min(crdR[x-1], crdG[x-1])

print(f"crdRGB -----")
for x in range(N):
    print(crdR[x], crdG[x], crdB[x])

print(min(crdR[N-1], crdG[N-1], crdB[N-1]))


#4. ############################################################################################################


dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]



N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

# 첫 집 초기화
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

# DP 진행
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

# 마지막 집에서 최소값
print(min(dp[N-1]))
