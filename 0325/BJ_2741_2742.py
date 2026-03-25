#2741

i = 1
N = int(input())

while i <= N:
    print(i)
    i += 1



'''

N=int(input())
for i in range(1,N+1):
    print(i)

'''




#2742 

N=int(input())
for i in reversed(range(1, N+1)):
    print(i)

'''

N = int(input())

# N부터 시작해서, 1까지 도달하려면 '0' 직전에서 멈춰야 함
for i in range(N, 0, -1):
    print(i)
    
'''

