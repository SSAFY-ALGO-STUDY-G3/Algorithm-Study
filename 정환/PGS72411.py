from itertools import combinations

def solution(orders, course):
    answer = []
    
    
    for k in course:
        tmp_dict = {}
        for j in orders:
            
            tmp = list(combinations(j, k))
            for i in tmp:
                inner = ''.join(sorted(i))
                if inner in tmp_dict:
                    tmp_dict[inner] += 1
                else:
                    tmp_dict[inner] = 1
        if tmp_dict:
            for a in tmp_dict:
                if tmp_dict[a] >= 2 and tmp_dict[a] == max(tmp_dict.values()):
                    if a not in answer:
                        answer.append(a)
            
    answer.sort()
    
    return answer
