def candies(n, arr):
    left = []
    right = []
    j = 0
    if arr[0] > arr[1]:
        left.append(2)
    else:
        left.append(1)
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            left.append(left[j]+1)
            j += 1
        else:
            left.append(1)
            j += 1
    if arr[-1] > arr[-2]:
        right.append(2)
    else:
        right.append(1)
    j = 0
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            right.append(right[j]+1)
            j += 1
        else:
            right.append(1)
            j += 1
    k = [max(left[x], right[n-x-1]) for x in range(n)]
    return sum(k)
