def climbingLeaderboard(scores, alice):
    ar = [1]
    j = 1
    score_num = len(scores)
    for i in range(score_num-1):
        if scores[i] == scores[i+1]:
            ar.append(ar[j-1])
            j += 1
            continue
        else:
            ar.append(ar[j-1]+1)
            j += 1
    result = []
    for k in range(len(alice)):
        if alice[k] >= scores[0]:
            result.append(1)
            continue
        elif alice[k] < scores[score_num-1]:
            result.append(ar[score_num-1]+1)
            continue
        else:
            flag = 0
            low = 0
            high = score_num
            while low <= high:
                mid = (low+high)//2
                if alice[k] == scores[mid]:
                    result.append(ar[mid])
                    flag = 1
                    break
                elif alice[k] > scores[mid]:
                    high = mid-1
                    continue
                else:
                    low = mid+1
                    continue
            if flag != 1:
                if alice[k] > scores[mid]:
                    result.append(ar[mid])
                else:
                    result.append(ar[mid+1])
    return result
