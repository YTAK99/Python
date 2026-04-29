def solution(answers):
    # 1. 각 수포자의 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]  # 각 수포자의 점수
    
    # 2. 채점
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            score[0] += 1
        if answers[i] == p2[i % len(p2)]:
            score[1] += 1
        if answers[i] == p3[i % len(p3)]:
            score[2] += 1
    
    # 3. 최대 점수
    max_score = max(score)
    
    # 4. 최고 점수 받은 사람 찾기
    result = []
    for i in range(3):
        if score[i] == max_score:
            result.append(i + 1)
    
    return result

#########################################################################################################

import itertools
def solution(answers):
    count1 = itertools.cycle([1,2,3,4,5])
    count2 = itertools.cycle([2,1,2,3,2,4,2,5])
    count3 = itertools.cycle([3,3,1,1,2,2,4,4,5,5])

    Ii=0
    Jj=0
    Kk=0
    

    for a,b in zip(answers,count1):
        if a == b:
            Ii+=1
    for c,d in zip(answers,count2):
        if c == d:
            Jj+=1
    for e,f in zip(answers,count3):
        if e == f:
            Kk+=1
    list1 = [Ii,Jj,Kk]
    hap = max(list1)
    result = []

    if list1[0] == hap:
        result.append(1)
    if list1[1] == hap:
        result.append(2)
    if list1[2] == hap:
        result.append(3)
    
    return result
